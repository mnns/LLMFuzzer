import os
import os.path
import requests
import yaml
import pyfiglet
from termcolor import colored

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
        
def printMotd():
    os.system('color') # windows patch
    print('Welcome to')
    print(colored(pyfiglet.figlet_format("LLM Fuzzer", font='starwars', justify='left', width=180), 'green'))   
    print(colored('### Warning: Use this LLM Fuzzer on your own LLM integrations!', 'red'))
    print(colored('### Do not attempt to harm or scan other LLMs!', 'red'))
    print()

class LLMfuzzer:
 
    def __init__(self, configPath):
        self.configPath = configPath
        print('! Loading config from: ' + configPath)
        
        # Check if config file exists
        if (not os.path.isfile(self.configPath)):
            raise Exception('Can''t read config file!')
            
        # Load YAML config
        self._loadConfig()

    def _loadConfig(self):
        with open(self.configPath, "r") as stream:
            try:
                self.config = yaml.safe_load(stream)                
            except yaml.YAMLError as exc:
                raise Exception('Can''t read config file!')
        
    def checkConnection(self):
        try:
            response = requests.post(
                self.config['Connection']['Url'], 
                json= { self.config['Connection']['Query-Attribute']: 'Print the capital of Brazil, in English.' }
            )
            
            if ('brasilia' not in response.text.lower()):
                raise Exception('Connection error, can''t continue evaluation.')
            print(colored('Success connecting to LLM via API', 'green'))
        except requests.exceptions.RequestException as e:
            raise Exception('Connection error, can''t continue evaluation.')
        
        
    def runAttack(self, path):
        attackConfig = ''
        with open(os.getcwd() + path, "r") as stream:
            try:
                attackConfig = yaml.safe_load(stream)                
            except yaml.YAMLError as exc:
                raise Exception('Can''t read attack file!')
        print(colored('Attack "' + attackConfig['Name'] + '" loaded. Running.', 'yellow'))
        
        for test in attackConfig['Tests']:
            try:
                response = requests.post(
                self.config['Connection']['Url'], 
                json={self.config['Connection']['Query-Attribute']: test['Query'] } )
                
                #Contains Check
                if (test['Comparer'] == 'Contains'):
                    #Check if any Output is in Response
                    if any(output.lower() in response.text.lower() for output in test['Output']):
                        if (test['Weight'] == 'Absolute'):
                            print(colored('LLM Vulnerabale to "' + attackConfig['Name'] + '"', 'red'))
                            break
            except requests.exceptions.RequestException as e:
                print('Connection error, can''t continue evaluation.')
                raise SystemExit(e)
        

        
    def runAttacks(self):
        # Fetch all chosen tests from config
        for attack in self.config['Attacks']:
            self.runAttack(attack['Path'])

