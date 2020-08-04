
from rasa_sdk.forms import FormAction
import urls
from rasa_sdk import Action, Tracker
import utils
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    AllSlotsReset,
    FollowupAction,
)
from rasa_sdk.executor import CollectingDispatcher
from customLogging import logger

#Corona Virus Hospital Finding Form

class coronaForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""
    # Returns name of form
    def name(self):
        return "corona_form"

    #Required slots to be filled for form
    @staticmethod
    def required_slots(tracker):
        return [
            "patient_name",
            "patient_email",
            "patient_phone",
            "patient_address",
            "patient_symptom",
            ]
    
    #Slot mappings to extract intents and entities from text
    def slot_mappings(self):
        
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"patient_name": self.from_entity(entity="patient_name",
                                            ),
                "patient_email": [self.from_entity(entity="patient_email",
                                                intent=["inform",
                                                        ]),
                               self.from_text()],
                "patient_address": [self.from_entity(entity="patient_address"),
                                    self.from_text()],
                "patient_phone": [self.from_entity(entity="patient_phone"),
                             self.from_text()],
                "patient_symptom": [self.from_entity(entity="patient_symptom"),
                             self.from_text()]}

    #Submit function to return data of hospitals
    def submit(
            self,
            dispatcher,
            tracker,
            domain,
        ):

        dispatcher.utter_message("Thanks for providing that info, we’ll help you troubleshoot that soon")
        return []

# Confirmed cases by State Action

class getConfirmedCasesOfState(Action):

    #Returns name of Action
    def name(self):
        return "state_confirmed_cases_action"
    
    #Returns number of confirmed cases by state as an int
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get confirmed Cases by state ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_confirmed_cases_by_state(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")

#Active Cases by State Action
class getActiveCasesOfState(Action):

    #Returns name of Action
    def name(self):
        return "state_active_cases_action"

    #Returns Active cases by state as an int
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get Active Cases by state ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_active_cases_by_state(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")

#Dead Cases by state Action
class getDeadCasesOfState(Action):
    #Returns name of action
    def name(self):
        return "state_dead_cases_action"
    
    #Returns number of dead cases by state as an integer
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get Dead Cases by state ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_dead_cases_by_state(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")

#Recovered Cases by state Action
class getRecoveredCasesOfState(Action):
    #Returns name of action
    def name(self):
        return "state_recovered_cases_action"
    
    #Returns number of recovered cases by state
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get Recovered Cases by state ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_recovered_cases_by_state(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")

#Recovered cases action by distruct
class getRecoveredCasesOfDistrict(Action):
    #Returns name of action
    def name(self):
        return "district_recovered_cases_action"
    
    #Returns recovered cases by district as an integer
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get Recovered Cases by District ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_recovered_cases_by_district(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")

#Active Cases by District Action
class getActiveCasesOfDistrict(Action):
    #Returns name of action
    def name(self):
        return "district_active_cases_action"
    
    #Returns number of active cases of district as an integer
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get Active Cases by District ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_active_cases_by_district(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")

#Dead Cases by District Action
class getDeadCasesOfDistrict(Action):
    #Returns name of action
    def name(self):
        return "district_dead_cases_action"
    
    #Returns number of dead cases by state as an integer
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get Dead Cases by District ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_dead_cases_by_district(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")

#Confirmed cases by District Action
class getConfirmedCasesOfDistrict(Action):
    #Returns name of action
    def name(self):
        return "district_confirmed_cases_action"
    
    #Returns number of confirmed vcases by district as an integer
    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
            logger.info("--- Get Confirmed Cases by District ---")
            ent = tracker.latest_message['entities']
            response2 = utils.get_confirmed_cases_by_district(ent[0]["value"])
            if response2:
                dispatcher.utter_message(text=str(response2))
            else: 
                dispatcher.utter_message(text="No Record found")
