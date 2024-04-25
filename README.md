https://github.com/machulav/ec2-github-runner/blob/main/README.md#save-costs


Deployment Instructions:
Access the Pre-Environment:

Log in to the CEFEO pre-environment using the provided URL: https://cefeo-us.pre.aws.us.corp
Ensure that the website banner is yellow, indicating the pre-environment.
Workspace Selection:

Navigate to the right corner and select the user XID.
Choose the workspace "CDO" from the options.
Search and Delete Existing Flows:

Search for the flow you intend to deploy. Use the JSON file name without extension for the search.
Example: If the JSON file name is '[Control Model] [Horizon US] Appian.json', search for "[Control Model] [Horizon US] Appian".
Once found, take a backup of the existing flow using the 'backup' button beside the flow name.
Open the flow and navigate to the dependencies section. Remove all dependencies as flows cannot be deleted if dependencies exist.
Delete the flow by clicking on the 'delete' button beside the flow.
Switch Workspace:

Change the workspace from 'CDO' to 'Control Model'.
Restore Backup and Deploy:

Click on the 'settings' button at the top right corner.
From the drop-down menu, select 'Restore backup'.
Choose the JSON file provided through release notes.
Click on 'Restore'. Ensure that all checkboxes are selected.
If there are any conflicts regarding environment variables, select the 'override' radio button and navigate to the 'Environment' tab.
Provide the environment variable values from the Excel sheet shared through release notes.
Click on 'Restore'.
Run Sample Flow:

Search for the newly deployed flow and click on the 'Launch' button beside its name.
Select the Target Datetime as the previous day and launch the flow.
Check Flow Status:

To monitor the flow's status, click on 'FlowLogs'.
Available statuses are QUEUED, RUNNING, COMPLETED, and FAILED.
Once the flow status is COMPLETED, consider the deployment successful.
In case of failure, communicate with the respective team members.
These instructions should guide you through the process of deploying ETL flows from one workspace to another using JSON files in the specified pre-environment.
