from tempfile import NamedTemporaryFile
import shutil
import csv
import json

# Logging the transaction that has taken place
def log_transaction(filename,log):
    log = json.dumps(log)
    with open(filename,'a') as csvF:
        csvWriter = csv.writer(csvF,delimiter = ' ')
        csvWriter.writerow([log])
        
# Marking the transaction as complete once it's been served.     
def mark_transaction_complete(filename,transaction,identifier):
    tempfile = NamedTemporaryFile(delete=False)
    final_list = []
    print("Mark transaction complete")
    with open(filename, 'rt') as csvFile,tempfile:
        reader = csv.reader(csvFile, delimiter=' ')
        writer = csv.writer(tempfile, delimiter=' ')
        for row in reader:
            row = ''.join(row)
            row = json.loads(row)
            k,_ = list(row.items())[0]
            if k == identifier:
                row[k]['completed'] = True
            rowed = json.dumps(row)           
            final_list.append(rowed)
    
    with open(filename, 'w') as tempfile:
        writer = csv.writer(tempfile, delimiter=' ')
        writer.writerows(final_list)
    shutil.move(tempfile.name, filename)  
    
# Return any unserved requests.    
def get_unserved_requests(file_name):
    with open(file_name,'rb') as csvF:
        transaction_log = csv.reader(csvF,delimiter = ' ')
        open_requests = []
        transaction_list = list(transaction_log)
        last_request = json.loads(transaction_list[len(transaction_list)-1][0])
        _,v = list(last_request.items())[0]
        if v['completed'] == False:
            return last_request
        else:
            return None