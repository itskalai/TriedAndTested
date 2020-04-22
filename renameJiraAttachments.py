#Rename the Jira Attachments from the ID names to the actual file names so it can be imported in another instance
import os
#top is the root of the attachments folder
top="/Users/kalaivani_ramasamy/importAttachments"
#list.txt contains the output of the query :
# select fa.id, fa.filename, ji.issuenum, p.pkey from fileattachment fa join jiraissue ji on ji.id= fa.issueid join project p on p.id = ji.project WHERE p.pkey = 'THIS;
with open("list.txt") as fh:
    for line in fh:
        if line.startswith("-"):
            continue
        else:
            id, file, ignore = line.split("|",2)
            for root, dirs, files in os.walk(top, topdown=False):
                for name in files:
                    if name in id.strip():
                        os.rename(os.path.join(root,name),os.path.join(root,file.strip()))
