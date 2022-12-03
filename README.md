# Hospital Automation System

Hospital Automation System provides lots of operations both for patients and doctors. 

## Table of contents
* [General info](#general-info)
* [Technologies-Tools](#technologies-tools)
* [Modules](#modules)
	* [Patient](#patient)
		* [Login - Sign Up](#login---sign-up)
		* [Appointment](#appointment)
		* [Appointment History](#appointment-history)
	* [Doctor](#doctor)
		* [Login](#login)
		* [Lab Request-Check](#lab-request-check)
		* [Patient Appointment History](#patient-appointment-history)
		* [Reports](#reports)
* [Setup](#setup)
* [Contact](#contact)




## General Info

Project scope includes patient and doctor operations such as appointment, appointment history of given patient information   (for doctor)  or logged in user, lab request and lab checks and reports of patients.
 
There are two types of user for the system. Doctor and patient. In the base page of the project, user choose the type of user to login. If it's doctor, login credentials already exists in database. If the user is patient, user must sign up with T.C. and password. 

After login, they can use the modules for operations.
	
![Base Page](https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/genel-giris.png?raw=true)
	
## Technologies-Tools
Project is created with:
* Python
* PyQt
* SqlLite DB Browser
* PyCharm

## Modules

All the modules in the project explained in this section.

These modules works with 4 different database table.
These are Patients, Doctors, Appointments, Lab Reports.

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/db-doctor.png?raw=true" alt="doctors" width="200"/>
<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/db-hastalar.png?raw=true" alt="patients" width="200"/>
<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/db-randevu.png?raw=true" alt="appointments" width="200"/>
<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/db-lab.png?raw=true" alt="labs" height="200"/>

### Patient
Modules that patients can use and operate.
#### Login - Sign Up
If the user has an account, can login directly, if not user must sign up from sign up page.

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/login.png?raw=true" alt="login" width="200" height="300" />
<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/user-sign-up.png?raw=true" alt="sign-up" width="300" height="300"/>


####  Appointment
Patinet appointment page to get appointment for free time of doctor. After successfully taking the appointment, the payment page will appear and after payment successfully taken then saves  the appointment to the database.

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/randevu-al.png?raw=true" alt="appointment" width="500" height="300"/>
<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/odeme.png?raw=true" alt="payment" width="300" height="300"/>

#### Appointment History

The logged in user can see their past appointments with this module.

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/hasta-gecmis-randevu.png?raw=true" alt="appointment-history" width="500" height="300"/>

### Doctor

Modules that doctors can use and operate.

#### Login
The doctor credentials are already in the database so there is no sign-up for doctors. If new doctor needs to append the database, admin adds it manually.

The login page is the same with patients.


<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/login.png?raw=true" alt="login" width="300" height="300" />

#### Lab Request-Check

Doctors can request for lab test such as urine test, blood test etc.

And check the status of the test from check page.

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/lab.png?raw=true" alt="lab" width="500" height="300" />

To request a test:
<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/lab-test.png?raw=true" alt="lab-test" width="300" height="300" />

To check the tests requested:

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/lab-check.png?raw=true" alt="lab-check" width="400" height="400" />

#### Patient Appointment History

Doctors can see the patients appointment history.
To do that, doctors should input the patients name and surname.

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/hasta-sorgu-rand2.png?raw=true" alt="patient-check" width="400" height="400" />

And the result for the given patient:

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/hasta-sorgu-rand.png?raw=true" alt="patient-check-result" width="400" height="400" />

#### Reports

Doctors can examine their appointment-patient reports. 

For every patient of doctor, it shows the number of appointments 

<img src="https://github.com/alibariszengin/Remedy-For/blob/master/HastaneSistemi/photos/HASTA-SORGU.png?raw=true" alt="hasta-sorgu" width="500" height="400" />

## Setup
To run this project, run from file explorer with clicking GirisE.exe  or after change directory to project folder, run 'GirisE.exe' on the terminal with your local database.

`$.\HastaneSistemi\GirisE.exe`


## Contact

Ali Barış Zengin  -  [alibariszengin@gmail.com](mailto:alibariszengin@gmail.com)

Project Link:  [https://github.com/alibariszengin/Remedy-For](https://github.com/alibariszengin/Remedy-For)

