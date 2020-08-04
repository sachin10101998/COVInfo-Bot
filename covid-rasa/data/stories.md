## greet

* greet
  - utter_greet

## thank

* thank
  - utter_noworries

## goodbye

* bye
  - utter_bye

## Some question from FAQ

* faq
    - respond_faq

## corona form
* corona
    - corona_form                   <!--Run the sales_form action-->
    - form{"name": "corona_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->

## New Story

* greet
    - utter_greet
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* corona
    - corona_form
    - form{"name":"corona_form"}
    - slot{"requested_slot":"patient_name"}
* inform{"patient_name":"Sachin chopra"}
    - slot{"patient_name":"Sachin chopra"}
    - corona_form
    - slot{"patient_name":"Sachin chopra"}
    - slot{"requested_slot":"patient_email"}
* inform{"patient_email":"sachinchopraftw@gmail.com"}
    - slot{"patient_email":"sachinchopraftw@gmail.com"}
    - corona_form
    - slot{"patient_email":"sachinchopraftw@gmail.com"}
    - slot{"requested_slot":"patient_phone"}
* inform{"patient_phone":"8755148310"}
    - slot{"patient_phone":"8755148310"}
    - corona_form
    - slot{"patient_phone":"8755148310"}
    - slot{"requested_slot":"patient_address"}
* inform{"patient_address":"2712 Jain colony, Moti nagar, Ludhiana"}
    - slot{"patient_address":"2712 Jain colony, Moti nagar, Ludhiana"}
    - corona_form
    - slot{"patient_address":"2712 Jain colony, Moti nagar, Ludhiana"}
    - slot{"requested_slot":"patient_symptom"}
* inform{"patient_symptom":"cough and fever"}
    - slot{"patient_symptom":"cough and fever"}
    - corona_form
    - slot{"patient_symptom":"cough and fever"}
    - form{"name":null}
    - slot{"requested_slot":null}


## handling faq qith form
* corona
    - corona_form
    - form{"name": "corona_form"}
* faq
    - respond_faq
    - corona_form
    - form{"name": null}


## Out of scope

* out_of_scope
    - utter_out_of_scope

## Confirmed cases by state
* stateconfirmedcases
    - state_confirmed_cases_action

## Active Cases by State
* stateactivecases
    - state_active_cases_action

## Dead Cases by State
* statedeadcases
    - state_dead_cases_action

## Recovered Cases By State
* staterecoveredcases
    - state_recovered_cases_action

## Confirmed Cases By District
* districtconfirmedcases
    - district_confirmed_cases_action

## Active Cases By district
* districtactivecases
    - district_active_cases_action

## Recovered Cases By district
* districtrecoveredcases
    - district_recovered_cases_action

## Dead Cases By district
* districtdeadcases
    - district_dead_cases_action
