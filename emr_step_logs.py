import sys
import subprocess
from collections import namedtuple
from functools import reduce
from pprint import pprint


queries = [
    "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9",
    "q10", "q11", "q12", "q13", "q14a", "q14b", "q15", "q16", "q17", "q18", "q19",
    "q20", "q21", "q22", "q23a", "q23b", "q24a", "q24b", "q25", "q26", "q27", "q28", "q29",
    "q30", "q31", "q32", "q33", "q34", "q35", "q36", "q37", "q38", "q39a", "q39b",
    "q40", "q41", "q42", "q43", "q44", "q45", "q46", "q47", "q48", "q49",
    "q50", "q51", "q52", "q53", "q54", "q55", "q56", "q57", "q58", "q59",
    "q60", "q61", "q62", "q63", "q64", "q65", "q66", "q67", "q68", "q69",
    "q70", "q71", "q72", "q73", "q74", "q75", "q76", "q77", "q78", "q79",
    "q80", "q81", "q82", "q83", "q84", "q85", "q86", "q87", "q88", "q89",
    "q90", "q91", "q92", "q93", "q94", "q95", "q96", "q97", "q98", "q99",
    "ss_max"
]

ShuffleLog = namedtuple("ShuffleLog", "schema, numFields, allFixedSized, allNonNull, numBytes, numRows")


def list_files(folder, pattern):
    return subprocess.run([f"fd -a -t f -e gz {pattern} ./{folder}"],
    shell=True, capture_output=True).stdout.decode("utf-8").split()


def search(file_paths, pattern):
    for f in file_paths:
        match = subprocess.run([f"zcat {f} | rg -o '{pattern}' "], shell=True, capture_output=True)
        if match.returncode == 0:
            yield (f, match.stdout.decode("utf-8").split("\n"))


def map_queries_steps(folder, query_pat):
    step_paths = list_files(f"{folder}/steps", 'stdout')

    acc = dict()
    for f,s in search(step_paths, f'Running execution {query_pat} iteration'):
        query_id = s[0].split()[2]
        step_id = next(filter(lambda x: x.startswith('s-'), f.split('/')))
        acc[query_id] = step_id

    return acc


def map_steps_apps(folder):
    step_paths = list_files(f"{folder}/steps", 'stderr')

    acc = dict()
    for f,s in search(step_paths, r'YarnClientSchedulerBackend: Application application_\w+ has started running'):
        app_id = s[0].split()[2]
        step_id = next(filter(lambda x: x.startswith('s-'), f.split('/')))
        acc[step_id] = app_id

    return acc


def process_line(line):
    parts = line.split('|')[1:]
    assert len(parts) == 6, f"illegal : {line}"
    
    schema, numFields, allFixedSized, allNonNull, numBytes, numRows = parts
    numFields = int(numFields)
    numBytes = int(numBytes)
    numRows = int(numRows)
    record = ShuffleLog(schema, numFields, allFixedSized, allNonNull, numBytes, numRows)

    return record

def add_logs(a, b):
    assert a.schema == b.schema, f"mismatch {a} {b}"
    assert a.numFields == b.numFields, f"mismatch {a} {b}"
    assert a.allFixedSized == b.allFixedSized, f"mismatch {a} {b}"
    assert a.allNonNull == b.allNonNull, f"mismatch {a} {b}"

    numBytes = a.numBytes + b.numBytes
    numRows = a.numRows + b.numRows
    return ShuffleLog(a.schema, a.numFields, a.allFixedSized, a.allNonNull, numBytes, numRows)


def reduce_logs(log_groups):
    return map(lambda logs: reduce(add_logs, logs), log_groups.values())


def parse_logs(app_files):
    log_groups = dict()
    for _,lines in search(app_files, 'insertRecordIntoSorterCounter.+'):
        for line in filter(bool, map(lambda s : s.strip(), lines)):
            record = process_line(line)
            if record.numBytes > 0 or record.numRows > 0:
                log_groups.setdefault(record.schema, []).append(record)

    return log_groups


def print_stats(query_id, log_stats, fout):
    for record in log_stats:
        line = '|'.join(map(str, record))
        print(f"{query_id}|{line}", file = fout)


def main(folder):
    query_pat = f"({'|'.join(queries)})"
    queries_steps = map_queries_steps(folder, query_pat)
    pprint(queries_steps)
    steps_apps = map_steps_apps(folder)
    pprint(steps_apps)

    with open(f"{folder}_report.csv", 'w') as fout:
        print(f"query|{'|'.join(ShuffleLog._fields)}", file = fout)

        for query_id in sorted(queries_steps.keys(), key = lambda k: queries.index(k)):
            step_id = queries_steps[query_id]
            app_id = steps_apps[step_id]
            pprint([query_id, step_id, app_id])

            app_files = list_files(f"{folder}/containers/{app_id}", 'stderr')
            log_groups = parse_logs(app_files)
            log_stats = reduce_logs(log_groups)
            print_stats(query_id, log_stats, fout)





if __name__ == "__main__":
    main(sys.argv[1])
