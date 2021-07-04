from datetime import datetime, timezone, timedelta
import time
import sys
import boto3

cloudwatch = boto3.client('logs')
logGroupName = "Prod/application.json.log"
queryString = 'filter message like "EMAIL MATCHING:" | fields message'
field = "message"
start = datetime(2021, 1, 29, tzinfo=timezone.utc)
end = datetime(2021, 3, 17, tzinfo=timezone.utc)

# only 10k log events can be fetched at a time, adjust duration accordingly
duration = timedelta(hours=1)

fout = open("out.logs", 'w')
matched = 0

#####

def extractFields(results):
    global matched
    for result in results:
        for item in result:
            if item["field"] == field:
                print(item["value"], file=fout)
                matched += 1


PENDING_STATUS = {"Scheduled", "Running"}
def fetchResults(queryId):
    time.sleep(1)
    response = cloudwatch.get_query_results(queryId=queryId)

    status = response["status"]

    if status == "Complete":
        results = response["results"]
        print(f"Found {len(results)} for {queryId}")
        extractFields(results)
    elif status in PENDING_STATUS:
        print(f"Waiting for {queryId}")
        fetchResults(queryId)
    else:
        print(queryId, response, file=sys.stderr)


def runSlice(startTime, endTime):
    response = cloudwatch.start_query(
        logGroupName=logGroupName,
        queryString=queryString,
        startTime=startTime,
        endTime=endTime,
        limit=10000
    )
    queryId = response["queryId"]
    print(f"Started {startTime} {endTime} {queryId}")
    fetchResults(queryId)
    print(f"Done {startTime} {endTime} {queryId}")



def runAll():
    start_epoch = int(start.timestamp())
    end_epoch = int(end.timestamp())
    delta = int(duration.total_seconds())

    while start_epoch < end_epoch:
        print(f"Processing {datetime.utcfromtimestamp(start_epoch)}")
        next_epoch = start_epoch + delta
        runSlice(start_epoch, next_epoch)
        start_epoch = next_epoch


#####

def main():
    runAll()
    print(f"Matched = {matched}")

if __name__ == '__main__':
    main()

