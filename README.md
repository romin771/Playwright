# Playwright and Pytest Test Automation Project

## Introduction

Welcome to my Playwright and Pytest-based Test Automation Project README! This is a small project I've created to showcase my knowledge of Playwright and the structured test architecture with a focus on the Page Object Model (POM).

## Project Description

This small project covers four straightforward test cases, each representing a specific scenario. Click on a scenario to see its details:

<details>
  <summary><b>Scenario 1: Unsuccessful Login</b></summary>

  **Test Case ID: TC-001**

  **Test Case Description**: Make sure the user cannot log in by providing the correct username and a wrong password.

  **Preconditions**:
  - An email that has already been registered correctly exists.
  - The user is logged out.

  **Test Steps**:

  1. **Step 1: Navigate to Userlike Website**
     - **Action**: Open a web browser and navigate to the Userlike website (https://www.userlike.com/en/).
     - **Expected Behavior**: The Userlike website should load successfully.

  2. **Step 2: Access Login Popup**
     - **Action**: Click on the "Log In" button.
     - **Expected Behavior**: A pop-up should appear, displaying email and password fields.

  3. **Step 3: Enter Correct Email Address**
     - **Action**: Enter a registered and correct email address into the email field.
     - **Expected Behavior**: The entered email address should be visible in the email field.

  4. **Step 4: Enter Wrong Password**
     - **Action**: Enter an incorrect password into the password field.
     - **Expected Behavior**: The entered password should be visible in the password field.

  5. **Step 5: Log In**
     - **Action**: Click the "Log In" button within the pop-up.
     - **Expected Behavior**: An error message should appear, stating "Wrong email or password." The user should not be able to navigate to the dashboard.

  **Pass Criteria**: The user cannot log in with a correct email and incorrect password, and an error message is displayed.

  **Fail Criteria**: The user is able to log in with incorrect credentials, or no error message is displayed.

<summary><b>Other Test Cases for Unsuccessful Login</b></summary>

    - Verify that the user cannot log in when they do not provide an email address.
    - Verify that the user cannot log in when they do not provide a password.
    - Verify that the user cannot log in when they provide an incorrect email address.
    - Verify that the user cannot log in when they provide an incorrect password.
    - Verify that the user cannot log in when they provide an email that is not registered in the system.
  </details>
</details>

<details>
  <summary><b>Scenario 2: Successful Login</b></summary>

  **Test Case ID: TC-002**

  **Test Case Description**: Verify that a user can successfully log in by providing the correct username and password.

  **Preconditions**:
  - An email that has already been registered correctly exists.
  - The user is logged out.

  **Test Steps**:

  1. **Step 1: Navigate to Userlike Website**
     - **Action**: Open a web browser and navigate to the Userlike website (https://www.userlike.com/en/).
     - **Expected Behavior**: The Userlike website should load successfully.

  2. **Step 2: Access Login Popup**
     - **Action**: Click on the "Log In" button.
     - **Expected Behavior**: A pop-up should appear, displaying email and password fields.

  3. **Step 3: Enter Email Address**
     - **Action**: Enter a registered email address into the email field.
     - **Expected Behavior**: The entered email address should be visible in the email field.

  4. **Step 4: Enter Password**
     - **Action**: Enter the corresponding password into the password field.
     - **Expected Behavior**: The entered password should be visible in the password field.

  5. **Step 5: Log In**
     - **Action**: Click the "Log In" button within the pop-up.
     - **Expected Behavior**: Upon successful login, the user should be navigated to the Userlike dashboard.

  **Pass Criteria**: The user successfully logs in, and the Userlike dashboard is displayed.

  **Fail Criteria**: The user encounters errors during the login process, or the dashboard is not accessible.
</details>

<details>
  <summary><b>Scenario 3: Create Widget Successfully</b></summary>

  **Test Case ID: TC-003**

  **Test Case Description**: Verify that the user can create a new widget successfully.

  **Preconditions**:
  - There should be a trial user registered and available.
  - For trial users, there should be fewer than 4 widgets available.
  - For trial users, there should be some days left from their trial.

  **Test Steps**:

  1. **Step 1: Navigate to Userlike Website**
     - **Action**: Open a web browser and navigate to the Userlike website (https://www.userlike.com/en/).
     - **Expected Behavior**: The Userlike website should load successfully.

  2. **Step 2: Log In Successfully**
     - **Action**: Log in successfully.
     - **Expected Behavior**: The user should navigate to the Userlike dashboard.

  3. **Step 3: Access Channels Menu**
     - **Action**: Click on "Channels" from the left menu.
     - **Expected Behavior**: The channels submenu should open.

  4. **Step 4: Access Website Widget Page**
     - **Action**: Click on "Website Widget" from the channels submenu.
     - **Expected Behavior**: The website widget details page should appear.

  5. **Step 5: Create New Widget**
     - **Action**: Click on the "Add Widget" button.
     - **Expected Behavior**: A "Create Widget" popup should appear.

  6. **Step 6: Confirm New Widget Creation**
     - **Action**: Click on the "Create Widget" button within the popup.
     - **Expected Behavior**: A new widget should be created, and the user should be able to copy and configure it.

  **Pass Criteria**: A new widget is successfully created, and the user can copy and configure it.
</details>

<details>
 <summary><b>Scenario 4: Delete the Latest Created Widget</b></summary>

  **Test Case ID: TC-004**

  **Test Case Description**: Make sure the user can delete the created widget successfully.

  **Preconditions**:
  - There should be a trial user registered and available.
  - There should be at least more than 2 widgets available.
  - For trial users, there should be some days left from their trial.

  **Test Steps**:

  1. **Step 1: Navigate to Userlike Website**
     - **Action**: Open a web browser and navigate to the Userlike website (https://www.userlike.com/en/).
     - **Expected Behavior**: The Userlike website should load successfully.

  2. **Step 2: Log In Successfully**
     - **Action**: Log in successfully.
     - **Expected Behavior**: The user should navigate to the Userlike dashboard.

  3. **Step 3: Access Channels Menu**
     - **Action**: Click on "Channels" from the left menu.
     - **Expected Behavior**: The channels submenu should open.

  4. **Step 4: Access Website Widget Page**
     - **Action**: Click on "Website Widget" from the channels submenu.
     - **Expected Behavior**: The website widget details page should appear.

  5. **Step 5: Delete Latest Created Widget**
     - **Action**: From the widget row list, click on the delete button on the top widget in the row.
     - **Expected Behavior**: A delete popup should appear.

  6. **Step 6: Confirm Widget Deletion**
     - **Action**: Click on the "Delete" button within the popup.
     - **Expected Behavior**: The widget should be removed successfully and get deleted from the widget rows.

  **Pass Criteria**: The latest created widget is successfully deleted from the widget rows.

  **Fail Criteria**: The widget deletion process encounters errors, or the widget is not removed from the widget rows.
</details>
While working with the application, there were some minor issues that happened with different severity levels. I will try to report them to you in order to showcase the way I report a bug to the development team. I will keep the list ordered by severity, from high to low.

## Bugs 

While working with the application, there were some minor issues that happened with different severity levels. I will try to report them to you in order to showcase the way I report a bug to the development team. I will keep the list ordered by severity, from high to low.

<details>
  <summary><b>Bug 1</b></summary>

  ### Bug 1: Crash on Deleting the Widget

  **Description:**
  A crash occurs when a user attempts to delete a widget and clicks the DELETE button multiple times or rapidly. The crash leads to a pop-up error message.

  **Reproduction Steps:**

  1. Log in to the application.
  2. Navigate to the dashboard where widgets are listed.
  3. Identify a widget that should be deleted.
  4. Click on the "Delete" button.
  5. Quickly click the "Delete" button again or click it multiple times.

  **Expected Behavior:**

  - Clicking the "Delete" button multiple times should not lead to a crash.
  - The system should prevent multiple clicks or actions on the button until the first action is successfully processed and a response is received.

  **Actual Behavior:**

  - Clicking the "Delete" button multiple times or rapidly leads to a crash.
  - A pop-up error message with the title "It looks like we're having issues" appears, prompting the user to enter additional information.


  **Attachments:**

  - Screen shots/logs/videos / etc. will be provided.
</details>

<details>
  <summary><b>Bug 2</b></summary>

 ### Bug 2: Website Widget Popup Won't Appear Correctly if We Scroll the Page Before Clicking on Add Widget Button

  **Description:**
  If a user navigates to the website widget section and, just before clicking the "Add widget" button, scrolls the page slightly to check the bottom of the page, the popup does not appear correctly on the screen. The screen becomes darker, but the popup is not visible without scrolling down. This results in a poor user experience that should be addressed.

  **Reproduction Steps:**

  1. Navigate to the Userlike website.
  2. Log in successfully.
  3. Go to the website widget page.
  4. Scroll the page upward slightly.
  5. Click on the "Add widget" button.

  **Expected Behavior:**

  - Regardless of whether the user scrolls the page, the popup should appear correctly on the screen, ensuring that the user can easily create a widget.

  **Actual Behavior:**

  - When the user scrolls the page before clicking the "Add widget" button, the page becomes darker, but the new widget popup does not appear correctly on the screen. To see the popup, the user must scroll down a bit.
</details>

<details>
  <summary><b>Bug 3</b></summary>

 ### Bug 3: Session Expiring Leads to User Experience Issues

  **Description**:
  If a user leaves a page for an extended period, causing their session to expire, it results in functionality issues. Users are unable to interact with the application correctly, and they can't rectify the issue without refreshing the page. For example, when on the website widget page, if the user's session expires, attempting to delete a widget results in nothing happening. Instead of the trash icon, a loading icon is displayed.

  **Reproduction Steps**:
  1. Navigate to the Userlike website.
  2. Log in successfully.
  3. Go to the website widget page.
  4. Leave the page unattended for an extended period to allow the session to expire.
  5. Click on the trash icon to remove a widget.

  **Expected Behavior**:
  - It would be helpful to display an error to the user after their session expires. This way, users can understand that they should refresh the page, avoiding confusion when using the service.

  **Actual Behavior**:
  - No error is shown, and the application's functionality doesn't work correctly after the session expires.
</details>
<details>
  <summary><b>Bug 4</b></summary>

 ### Bug 4: Typo in Organizations Description

  **Description**:
  In the organization description, there is a typo in the text:
  "You can manage multiple organizations in one account. Each organization has its own configuration, i.e. its own Widgets, operator accounts, macros and so on. You current plan only supports one default organization."

  The phrase "You current plan" should be corrected to "Your current plan."

  **Reproduction Steps**:
  1. Navigate to the Userlike website.
  2. Log in successfully.
  3. Go to the account section.
  4. Access the organizations page.

  **Expected Behavior**:
  - The text should read "your current account."

  **Actual Behavior**:
  - The text displays "you current account."





