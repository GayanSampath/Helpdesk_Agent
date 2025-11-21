AI Helpdesk Automation Research Plan
Prepared by: Gayan Sampath
1. Introduction

Modern IT helpdesk operations involve repetitive troubleshooting tasks that consume significant engineering time. As organizations scale, proactive system monitoring and automated remediation become essential. This research explores the development of an AI-powered Helpdesk Automation Bot capable of:

Identifying laptop/system issues

Performing automated fixes

Predicting future failures

Sending alerts when human intervention is required

The goal is to improve IT operational efficiency, reduce downtime, and introduce predictive maintenance capabilities within the helpdesk environment.

2. Objective of the Project

The primary objective of this research is to design and prototype an AI-driven local agent that runs on each laptop and:

Monitors system health (CPU, RAM, storage, event logs, services)

Detects issues using AI-based anomaly detection

Executes automated remediation using Python + PowerShell

Predicts upcoming failures using machine learning

Notifies the IT team via email/Teams/Slack/WhatsApp

Integrates with Microsoft Active Directory for access control and deployment

The proof-of-concept will initially be deployed and tested within the ECG team.

3. Scope of Research

This research project will focus on:

3.1 Monitoring Capabilities

System resource usage

Event viewer logs

Service health

Network issues

Application-specific diagnostics

Disk space and SMART indicators

3.2 Automated Fixes

The bot will execute pre-approved scripts to fix common issues:

Restart stuck services

Clear temporary files

Reset Outlook/Teams

Fix network adapters

Clean Windows Update cache

Kill high CPU processes

3.3 AI Detection & Prediction

AI algorithms will be used for:

Anomaly detection

Failure prediction

Trend analysis

Pattern matching in logs

3.4 Notifications

If the bot cannot fix an issue, it will escalate by:

Sending email

Creating helpdesk ticket

Sending Teams/Slack messages

Logging issues to a central database

4. Proposed Architecture

The system is composed of the following layers:

Local Monitoring Agent

AI Decision Engine

Auto-Remediation Framework

Notification Layer

Central Management (Optional future expansion)

Active Directory Integration

5. Tools & Technologies

Python (main agent logic)

PowerShell (system fixes on Windows)

Scikit-learn / TensorFlow (AI models)

psutil (system monitoring)

SMTP / Teams Webhook / WhatsApp API

Active Directory (deployment, authentication)

GitHub (source control)

6. Expected Outcomes

Reduced workload for helpdesk engineers

Faster issue resolution

Proactive maintenance

Increased stability of employee laptops

A reusable and scalable AI-based IT support framework

A strong project portfolio piece for AI/DevOps career transition

7. Future Enhancements

Central admin dashboard

Aggregate logs for all employees

Cloud-based model training

Integration with SIEM tools

Auto-ticket creation in Jira/ServiceNow

8. Conclusion

This research project is a practical approach to combining AI, automation, and IT support engineering. The resulting AI Helpdesk Bot will not only demonstrate strong technical skills but also deliver real value by improving helpdesk performance and reducing manual workload.

📑 End of Document