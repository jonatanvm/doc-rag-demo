import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader

documents = SimpleWebPageReader(html_to_text=True).load_data(
    [
        "https://elevenlabs.io/docs/product/speech-synthesis/overview",
        "https://elevenlabs.io/docs/conversational-ai/libraries/conversational-ai-sdk-python",
        "https://elevenlabs.io/docs/conversational-ai/libraries/conversational-ai-sdk-react",
        "https://elevenlabs.io/docs/conversational-ai/libraries/conversational-ai-sdk-js",
        "https://elevenlabs.io/docs/conversational-ai/libraries/conversational-ai-sdk-swift",
        "https://elevenlabs.io/docs/conversational-ai/docs/agent-setup"
     ]
)

index = SummaryIndex.from_documents(documents)

# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("Does conversational ai have a rag native SDK")

text_response = response.response

source_text = [source.text for source in response.source_nodes]
ref_doc_ids = [source.node.ref_doc_id for source in response.source_nodes]

print("done")
