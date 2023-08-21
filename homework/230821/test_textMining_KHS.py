
from collections import defaultdict, OrderedDict

text = '''
Die Deutschen sorgen sich um ihre Wirtschaft –
und favorisieren auch deshalb die AfD.
In den USA waren es ebenfalls ökonomische Fragen,
die Donald Trump ins Weiße Haus brachten. Joe Biden hat das erkannt –
und setzt auf „Bidenomics“. Ein Blick auf die Strategie lohnt sich auch für jeden Deutschen.

Der Nordwesten des US-Bundesstaats Georgia war vergessen.
Zurück auf die politische Landkarte brachte ihn erst der Aufstieg einer rechtsextremen Politikerin.
In der Region am Fuße der Appalachen, gekennzeichnet vom jahrzehntelangen Verfall der Textilindustrie,
wurde 2020 die Republikanerin Marjorie Taylor-Greene ins Repräsentantenhaus gewählt.
Die Politikerin fiel auf mit antisemitischen Verschwörungstheorien und Sympathien für Mordfantasien gegen demokratische Politiker.
 Trotzdem verteidigte sie 2022 souverän ihr Mandat. Demokraten haben in dem Wahlkreis keine Chance.

Das versucht US-Präsident Joe Biden zu ändern – mit den sogenannten „Bidenomics“.
Im Zentrum steht ein gigantisches Subventionsprogramm, der „Inflation Reduction Act“ (IRA).
Der Staat verteilt dabei über zehn Jahre hinweg 370 Milliarden Dollar.
Der Fokus liegt auf den abgehängten Regionen im Landesinneren – 
wo die Demokraten jahrzehntelang kaum politische Angebote machten.
Es ist ein ökonomisches „America first“. Gigantische Subventionen, damit Jobs in den USA bleiben und entstehen.
 Damit es Durchschnitts-Amerikanern besser geht – und der Trumpismus seinen Zauber verliert.

43 Prozent nennen „Wirtschaft“

Die Globalisierung hatte zur Abwanderung Hunderttausender Jobs aus den USA geführt.
Trump hatte dann im Jahr 2016 das Rezept gefunden, Wut und Frust jener Menschen zu kanalisieren, die den wirtschaftlichen Abstieg hinter sich haben oder ihn fürchten.
Seine damalige Gegenkandidatin Hillary Clinton hatte diese Wähler nicht gesehen – Biden hat sie genau im Blick.

Der Zusammenhang zwischen wirtschaftlicher Lage und einem Erstarken rechtsnationalistischer Politik-Angebote rückt auch in Deutschland in den Fokus.
Die Sorge um einen Abstieg der Bundesrepublik geht einher mit einem Höhenflug der AfD.
In einer Umfrage von Infratest Dimap nannten 43 Prozent „Wirtschaft“ als Grund,
aktuell die Rechtsaußen-Partei wählen zu wollen. Nur Zuwanderung (65 Prozent) und Energiepolitik (47 Prozent) wurden häufiger genannt.
Auch wenn sich Deutschland und die USA in vielen Punkten unterscheiden: ein Blick auf das Experiment jenseits des Atlantiks lohnt.
'''.lower().split()


word_count = defaultdict(lambda: 0)

for word in text:
    word_count[word] += 1

# 단어 빈도수에 따라 정렬된 OrderedDict 생성
sorted_word_count = OrderedDict(
    sorted(word_count.items(), key=lambda t: t[1], reverse=True))

# 상위 10개 단어와 그 빈도수 출력
top_10_words = list(sorted_word_count.items())[:10]

print("상위 10개 단어와 빈도수:")
for word, count in top_10_words:
    print(f"단어: {word}, 빈도수: {count}")
