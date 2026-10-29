CloudOps — Self-Service Deployment Platform



1 Purpose



Build a command-line tool that automates the deployment of a sample web application using repeatable, testable, and secure processes.



2 Business Problem



Manual deployment processes can be inconsistent and time-consuming. Deployment failures may be difficult to diagnose, and engineers may need to repeat the same steps manually.



CloudOps aims to improve deployment consistency, automate repetitive tasks, detect failures early, and provide useful diagnostic information.



3 Business Objectives



Reduce manual deployment steps.

Make deployments consistent and repeatable.

Detect invalid requests and failed checks early.

Make deployment failures easier to diagnose.

Provide clear deployment status and application health information.

Demonstrate practical DevOps engineering skills through a working project.



4 Functional Requirements



FR-01 - Request Validation



The CLI must accept a deployment target and revision, validate the supplied inputs, and reject invalid requests with useful error messages.



FR-02 - Source Control



The system must retrieve the intended source revision and identify what is being deployed.



FR-03 - Automated Testing



The system must run the required automated tests and prevent deployment when mandatory checks fail.



FR-04 - Containerisation



The system must build a Docker image for the sample application.



FR-05 - Deployment



The system must deploy the container locally using a repeatable process.



FR-06 - Health Verification



The system must check whether the deployed application responds successfully.



FR-07 - Status and Diagnostics



The CLI must report success or failure, provide useful logs, and return an appropriate exit code.



FR-08 - Failure Handling



The system must handle expected failures without silently reporting success. Recovery procedures must be documented.



5 Non-Functional Requirements



Security



Validate inputs, avoid exposing secrets, and minimise privileges.



Reliability



Failed mandatory checks must prevent deployment from proceeding.



Maintainability



Use modular Python code, automated tests, and clear documentation.



Reproducibility



Document the environment and deployment procedure so another developer can reproduce the workflow.



Cost Control



Develop locally first and avoid unnecessary cloud resources or costs.



Observability



Make application health, deployment status, and errors diagnosable through logs and status information.



6 Initial Project Scope



Included



One sample web application.

Python-based CLI.

Git-based source control.

Automated testing.

Docker image building.

Local container deployment.

Application health checks

Logging and error handling.

Technical documentation and troubleshooting instructions.



Deferred



Graphical web portal.

Multiple application types and languages.

Multi-cloud deployment.

Enterprise high availability.

Public production hosting.



These features may be considered in later phases if they support the project objectives.



7 Acceptance Criteria



The initial release will be accepted when:



1 A valid request can complete the defined deployment workflow.

2 The deployed application passes its health check.

3 Invalid inputs produce clear error messages.

4 A failed mandatory test prevents deployment.

5 Deployment failures are visible and diagnosable.

6 Automated tests cover important success and failure scenarios.

7 Setup, usage, architecture, security limitations, and troubleshooting are documented.

8 Another developer can reproduce the workflow using the documented instructions.



8 Planned Technology Stack



Python: CLI development and deployment automation.

Git and GitHub: Version control and source-code management.

pytest: Automated testing.

Docker: Container image building and execution.

Linux and Bash: System operations and troubleshooting.

GitHub Actions: Continuous integration and automated checks.

Terraform: Infrastructure as code in a later phase.



Additional technologies will be introduced when justified by the architecture and project requirements.



9 Development Approach



Development will proceed incrementally:



1 Establish requirements and architecture.

2 Create the project structure and CLI foundation.

3 Implement the sample web application and tests.

4 Build and deploy the application using Docker.

5 Integrate health checks, logging, and failure handling.

6 Introduce CI/CD and security checks.

7 Explore infrastructure as code and cloud deployment.

8 Complete operational documentation and portfolio review.



10 Known Limitations and Risks



This is a portfolio project, not a claim of production readiness.



Potential risks include insecure input handling, deployment failures, incorrect health checks, exposed secrets, and unexpected cloud costs.



Unimplemented requirements, security limitations, operational risks, and known defects must be documented honestly.



11  Definition of Done



A feature is complete only when:



Its requirements and acceptance criteria are satisfied.

Relevant automated tests pass.

Expected failure scenarios have been considered.

The implementation is reviewed.

Required documentation is updated.

Actual results and known limitations are recorded.



12 Current Status



Phase: Requirements and project foundation.



\[x] Initialise the local Git repository.

\[x] Create the initial project directories.

\[x] Draft the requirements document.

\[x] Create the README.

\[ ] Complete the architecture documentation.

\[ ] Implement the CLI.

\[ ] Add automated tests.

\[ ] Build and deploy the sample application using Docker.

\[ ] Integrate CI/CD and operational diagnostics.



