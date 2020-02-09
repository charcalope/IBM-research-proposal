from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bert-base-srl-2019.06.17.tar.gz")

sentence = "Cell cycle- and  apoptosis-associated proteins were semi-quantified by Western Blotting and breakdown of mitochondrial membrane potentials was detected by JC-1 staining."
words = sentence.split()
spans = []

model_output = predictor.predict(sentence=sentence)
verb_list = model_output['verbs']
for verb in verb_list:
    print(verb)
    print()
