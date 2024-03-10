# SERVER OUTAGE INCIDENT REPORT

On March 10, 2024, our server encountered a problem, returning a 500 error. 
The log files did not provide useful information to identify the root cause of the issue.
This postmortem aims to document the problem, its resolution, and preventive measures to avoid similar incidents in the future.

# Timeline
•	Incident Detected: March 10, 2024, at 08:43 AM (GMT+1)
•	Incident Resolution: March 10, 2024, around 09:32 AM (GMT+1)

# Root Cause
The root cause of the error was a server misconfiguration.
The server stopped because of a corrupted or broken .htaccess file.
This might have happened during plugin installation or file configuration.
This caused the server to malfunction and return a status code of 500.

# Resolution
In order to resolve the problem, the .htaccess file was located and accessed via SFTP.
There was an improper structure with the .htaccess file.This was immediately edited.
After applying this fix, the server started functioning correctly, and the status code 500 error was resolved.

# Preventive Measures
To prevent similar incidents in the future, the following measures have been implemented:
•	Regular code review to check the config files before deployment and check for other errors.
•	Regular monitoring of servers to ensure they are running efficiently.
•	Ensure there are backup severs to prevent all of our services from being down during an issue.
