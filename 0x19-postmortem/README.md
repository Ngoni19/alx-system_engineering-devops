

## Postmortem Report

#### Issue Summary
On 5 March 2023, from 5:00 PM to 7:30 PM GMT, the company's online gaming website experienced an outage, rendering the website inaccessible to all users. 100% of the users were unable to access the website during the outage.

#### Timeline
* 5:00 PM: The issue was first detected when the monitoring system sent an alert to the engineering team.
* 5:05 PM: Engineers started investigating the issue and assumed it was due to network failure
* 5:15 PM: The network team was notified and they started investigating it as well
* 5:30 PM: The network team ruled out any network issues and informed the engineering team the problem might be related to the web server
* 5:45 PM: The engineering team started investigating the webserver and realized the server was overloaded with requests.
* 6:15 PM: The team increased the server capacity, but didn't resolve the issue.
* 6:30 PM: The team realized that the database was the bottleneck and started investigating the database server.
* 7:00 PM: The database server was restarted, which fixed the issue.
* 7:30 PM: The website was restored to normal operation


#### Root Cause and Resolution
> 
The root cause of the issue was an overload database server, causing it to fail. The increased traffic on the website was not anticipated, and the database server was not adequately provisioned to handle the increased load. The issue was resolved:  by restarting the database server, which cleared the overloaded connections and allowed the website to function correctly.


#### Corrective and Preventative Measures
After a discussion it has been decided we can prevent this in the future by:
* Reviewing and updating the website's capacity planning and provisioning process to ensure it can handle increased traffic loads.
* Implementing better monitoring systems to detect performance issues before they escalate to an outage
* Conduct regular load testing to identify and address bottlenecks before they become a problem.
* Implement database clustering to distribute traffic across multiple servers to reduce the likelihood of a single point of failure, to prevent exactly what happened now.
* Conduct a post-incident review to identify areas for improvement and make changes accordingly.

This is only a small incident so we are doing great! Thanks for your patience and your continued confidence in us.
