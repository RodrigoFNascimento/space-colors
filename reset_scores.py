import pandas as pd

def reset_scores():
    data = {'Player': ['rod', 'nya', 'chl', 'jck', 'thr'],
            'Points': [2000, 1500, 1000, 800, 600]}
    scores = pd.DataFrame(data, columns=['Player', 'Points'])
    scores.index += 1
    scores.to_csv('high scores.csv', index=False)

reset_scores()
