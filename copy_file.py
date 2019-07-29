import shutil
import os
import glob

def copy_jtls(final_jtl):
    with open(final_jtl, 'w') as outfile:
        outfile.write('timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,sentBytes,grpThreads,allThreads,URL,Latency,IdleTime,Connect\n')
        for file_name in glob.glob('*.jtl'):
            if file_name == final_jtl:
                # don't want to copy the jtls into the final jtl
                continue
            lines = open(file_name).readlines()
            with open(file_name, 'r') as jtl_file:
                for line in lines[1:]:
                    outfile.write("%s" % line)
                #shutil.copyfileobj(lines[1:], outfile)
