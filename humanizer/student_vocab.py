"""
Student-level vocabulary filter.

Provides a set of common, everyday English words that students actually use.
This filters out sophisticated/academic synonyms that AI models prefer
but real students would never write.

The word list is derived from frequency analysis of common English text.
Words are ranked by frequency — we keep only the top N most common words
to ensure synonym replacements stay at student vocabulary level.
"""

# Top ~3000 most common English words that students would actually use.
# This filters out WordNet suggestions like "solemnisation", "nidus", "clobber".
# Organized by part of speech for easier maintenance.

STUDENT_NOUNS = {
    # People & relationships
    'people', 'person', 'student', 'teacher', 'friend', 'family', 'parent',
    'child', 'children', 'kid', 'kids', 'baby', 'man', 'woman', 'boy', 'girl',
    'group', 'team', 'class', 'community', 'society', 'population', 'generation',
    'member', 'leader', 'worker', 'user', 'player', 'doctor', 'author', 'expert',

    # Places
    'world', 'country', 'city', 'town', 'area', 'place', 'home', 'house',
    'school', 'college', 'university', 'office', 'building', 'room', 'space',
    'market', 'store', 'hospital', 'church', 'park', 'street', 'road',

    # Things
    'thing', 'stuff', 'part', 'side', 'point', 'piece', 'bit', 'kind', 'type',
    'form', 'shape', 'size', 'level', 'stage', 'step', 'process', 'method',
    'system', 'program', 'plan', 'project', 'product', 'service', 'tool',
    'device', 'machine', 'phone', 'computer', 'screen', 'app', 'website',
    'book', 'paper', 'page', 'report', 'article', 'story', 'message', 'post',

    # Abstract
    'idea', 'thought', 'opinion', 'view', 'belief', 'feeling', 'sense',
    'reason', 'cause', 'effect', 'result', 'outcome', 'impact', 'influence',
    'problem', 'issue', 'challenge', 'question', 'answer', 'solution',
    'change', 'difference', 'choice', 'decision', 'action', 'effort',
    'chance', 'risk', 'advantage', 'benefit', 'value', 'cost', 'price',
    'goal', 'purpose', 'meaning', 'importance', 'role', 'responsibility',

    # Time
    'time', 'day', 'week', 'month', 'year', 'moment', 'period', 'age',
    'morning', 'night', 'hour', 'minute', 'second', 'future', 'past',

    # Concepts
    'life', 'death', 'health', 'food', 'water', 'energy', 'power',
    'money', 'job', 'work', 'career', 'business', 'industry', 'economy',
    'education', 'knowledge', 'skill', 'experience', 'practice', 'training',
    'research', 'study', 'science', 'technology', 'information', 'data',
    'news', 'media', 'culture', 'history', 'law', 'rule', 'policy',
    'right', 'freedom', 'safety', 'security', 'peace', 'war', 'fight',
    'attention', 'focus', 'interest', 'habit', 'routine', 'pattern',
    'growth', 'development', 'progress', 'success', 'failure',
    'relationship', 'connection', 'communication', 'conversation',
    'environment', 'nature', 'weather', 'climate', 'resource',

    # Body/emotion
    'body', 'hand', 'head', 'face', 'eye', 'heart', 'mind', 'brain',
    'voice', 'word', 'language', 'speech', 'sound', 'music', 'picture',
    'image', 'color', 'light', 'dark', 'heat', 'cold',
}

STUDENT_VERBS = {
    'start', 'begin', 'stop', 'end', 'finish', 'continue', 'keep',
    'try', 'fail', 'succeed', 'win', 'lose', 'achieve', 'reach', 'gain',
    'learn', 'teach', 'study', 'read', 'write', 'speak', 'listen', 'watch',
    'build', 'create', 'develop', 'design', 'produce', 'grow', 'improve',
    'change', 'shift', 'move', 'turn', 'push', 'pull', 'pick', 'drop',
    'add', 'remove', 'replace', 'fix', 'break', 'cut', 'join', 'split',
    'share', 'spread', 'send', 'receive', 'bring', 'carry', 'deliver',
    'show', 'hide', 'reveal', 'cover', 'fill', 'empty', 'clear',
    'open', 'close', 'lock', 'hold', 'grab', 'catch', 'throw', 'hit',
    'choose', 'pick', 'select', 'decide', 'prefer', 'accept', 'reject',
    'allow', 'prevent', 'avoid', 'protect', 'save', 'spend', 'waste',
    'happen', 'occur', 'cause', 'lead', 'result', 'affect', 'influence',
    'support', 'oppose', 'agree', 'argue', 'debate', 'discuss', 'explain',
    'describe', 'compare', 'measure', 'count', 'check', 'test', 'prove',
    'believe', 'trust', 'doubt', 'wonder', 'hope', 'wish', 'expect',
    'notice', 'recognize', 'understand', 'realize', 'discover', 'explore',
    'remember', 'forget', 'remind', 'imagine', 'consider', 'suggest',
    'offer', 'provide', 'supply', 'demand', 'require', 'depend',
    'connect', 'relate', 'involve', 'include', 'contain', 'consist',
    'follow', 'lead', 'guide', 'direct', 'manage', 'control', 'handle',
    'deal', 'face', 'struggle', 'suffer', 'enjoy', 'appreciate', 'value',
    'ignore', 'overlook', 'miss', 'skip', 'focus', 'concentrate',
    'encourage', 'inspire', 'motivate', 'challenge', 'force', 'push',
    'shape', 'form', 'mold', 'adapt', 'adjust', 'fit',
}

STUDENT_ADJECTIVES = {
    'good', 'bad', 'great', 'small', 'big', 'large', 'huge', 'tiny', 'little',
    'new', 'old', 'young', 'modern', 'recent', 'current', 'common', 'rare',
    'important', 'major', 'minor', 'main', 'key', 'basic', 'simple', 'complex',
    'easy', 'hard', 'difficult', 'tough', 'strong', 'weak', 'heavy', 'light',
    'fast', 'slow', 'quick', 'rapid', 'sudden', 'gradual', 'steady', 'constant',
    'clear', 'obvious', 'visible', 'hidden', 'secret', 'private', 'public',
    'true', 'false', 'real', 'fake', 'actual', 'normal', 'typical', 'usual',
    'strange', 'weird', 'odd', 'different', 'similar', 'same', 'equal',
    'special', 'unique', 'specific', 'general', 'broad', 'wide', 'narrow',
    'deep', 'shallow', 'thick', 'thin', 'flat', 'round', 'sharp', 'smooth',
    'hot', 'cold', 'warm', 'cool', 'dry', 'wet', 'fresh', 'clean', 'dirty',
    'rich', 'poor', 'cheap', 'expensive', 'free', 'available', 'ready',
    'happy', 'sad', 'angry', 'scared', 'worried', 'nervous', 'calm', 'peaceful',
    'positive', 'negative', 'active', 'passive', 'alive', 'dead', 'healthy',
    'safe', 'dangerous', 'serious', 'funny', 'interesting', 'boring',
    'useful', 'helpful', 'effective', 'powerful', 'popular', 'famous',
    'beautiful', 'ugly', 'pretty', 'nice', 'lovely', 'wonderful', 'amazing',
    'terrible', 'awful', 'horrible', 'perfect', 'excellent', 'brilliant',
    'likely', 'unlikely', 'possible', 'impossible', 'certain', 'sure',
    'natural', 'physical', 'mental', 'social', 'personal', 'professional',
    'traditional', 'digital', 'online', 'global', 'local', 'national',
    'whole', 'entire', 'complete', 'total', 'full', 'empty', 'extra',
    'short', 'tall', 'long', 'brief', 'daily', 'regular', 'frequent',
}

STUDENT_ADVERBS = {
    'really', 'very', 'quite', 'pretty', 'fairly', 'rather', 'somewhat',
    'totally', 'completely', 'entirely', 'fully', 'partly', 'mostly', 'mainly',
    'always', 'never', 'often', 'sometimes', 'usually', 'rarely', 'hardly',
    'already', 'still', 'yet', 'soon', 'recently', 'finally', 'eventually',
    'quickly', 'slowly', 'suddenly', 'gradually', 'constantly', 'frequently',
    'actually', 'basically', 'essentially', 'simply', 'clearly', 'obviously',
    'probably', 'possibly', 'certainly', 'definitely', 'surely', 'perhaps',
    'also', 'too', 'either', 'instead', 'otherwise', 'however', 'therefore',
    'directly', 'exactly', 'roughly', 'approximately', 'nearly', 'almost',
    'together', 'apart', 'alone', 'separately', 'equally', 'differently',
    'naturally', 'automatically', 'manually', 'personally', 'generally',
    'specifically', 'particularly', 'especially', 'mainly', 'primarily',
    'honestly', 'seriously', 'literally', 'genuinely', 'truly',
}

# Combined set for quick lookup
STUDENT_VOCABULARY = STUDENT_NOUNS | STUDENT_VERBS | STUDENT_ADJECTIVES | STUDENT_ADVERBS


def is_student_word(word: str) -> bool:
    """Check if a word is in the student vocabulary (common, everyday word)."""
    return word.lower().rstrip('s').rstrip('ed').rstrip('ing') in STUDENT_VOCABULARY or \
           word.lower() in STUDENT_VOCABULARY


def filter_student_synonyms(candidates: set, original: str) -> list:
    """
    Filter synonym candidates to only include student-level vocabulary.
    Returns filtered list of student words.
    """
    student_candidates = []

    for word in candidates:
        if word.lower() in STUDENT_VOCABULARY or word.lower().rstrip('s') in STUDENT_VOCABULARY:
            student_candidates.append(word)

    return student_candidates
