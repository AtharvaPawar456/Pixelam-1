# pip install sumy

text = "seems you're trying to summarize important periods in Indian history and connect them to cultural developments. While your text contains some inaccuracies and typos, the general idea is correct. Let's clarify and organize the information: **Early Civilization and Vedic Period:** * **Indus Valley Civilization (c. 3300-1300 BCE):** This early civilization in the Indian subcontinent was known for its advanced urban planning, sophisticated drainage systems, and written script that is yet to be deciphered. * **Vedic Period (c. 1500-500 BCE):** This period saw the emergence of the Vedas, sacred texts that formed the foundation of Hinduism. The Vedic texts introduced concepts like karma, dharma, and reincarnation, shaping Indian philosophy and spirituality. **Empires and Cultural Flourishing:** * **Mauryan Empire (c. 322-185 BCE):** Founded by Chandragupta Maurya, this empire unified most of the Indian subcontinent. Emperor Ashoka, known for his conversion to Buddhism, promoted peace and non-violence, leaving behind edicts inscribed on pillars and rocks throughout the empire. * **Gupta Empire (c. 320-550 CE):** This period is often referred to as a 'Golden Age' due to its flourishing in science, art, literature, and mathematics. Notable advancements were made in astronomy, medicine, and mathematics. **Later Dynasties and Mughal Rule:** * **Mughal Empire (1526-1857):** Founded by Babur, the Mughals ruled over much of India for centuries. They were known for their architectural marvels like the Taj Mahal and contributed to a rich cultural blend of Persian and Indian traditions. **Colonial Period and Independence:**"

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def textSummary(text):
    # Initialize the parser with your text
    text = text.replace('*', '').replace('$', '').replace('#', '')

    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Initialize the LexRank summarizer
    summarizer_lex = LexRankSummarizer()

    # Summarize using LexRank
    summary = summarizer_lex(parser.document, 6)

    # Concatenate the summary sentences into a string
    lex_summary = ""
    for sentence in summary:
        lex_summary += str(sentence) + " "
    
    return lex_summary

print(textSummary(text))
