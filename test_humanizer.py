from humanizer.pipeline import humanize_text
import json

sample = '''It is important to note that in order to ensure that the system leverages a comprehensive and robust framework, we must utilize every available resource to facilitate the seamless operation of all components. This is exactly why the proposed system is designed to be highly effective and extremely helpful for all users. The existing approach has been implemented to address a significant number of challenges that are faced on a daily basis. Furthermore, it is worth noting that all students will definitely benefit from this solution, as it completely eliminates the need for manual processes and always ensures data accuracy. There is no doubt that this will transform the way counsellors work, and it will certainly provide them with better tools to manage their workflow in a more efficient manner.'''

result = humanize_text(sample)
print('ORIGINAL:')
print(sample)
print('\nHUMANIZED:')
print(result['text'])
print('\nSTATS:')
for k,v in result['stats'].items():
    if v > 0:
        print(f'  {k}: {v}')
print(f"  TOTAL: {result['stats']['total_changes']}")
