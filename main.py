import llmfuzzer

# Print MOTD
llmfuzzer.printMotd()
   
# Create llmfuzzer instance
llmfuzzer = llmfuzzer.LLMfuzzer("llmfuzzer.cfg")

# Check for basic connection to LLM API
llmfuzzer.checkConnection()

# Run all tests
llmfuzzer.runAttacks()