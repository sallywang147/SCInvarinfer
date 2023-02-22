import click
import os
import joblib
import pandas as pd
#from settings import PROJECT_ROOT
from xgboost import XGBClassifier
#from sklearn.external import joblib
from transformers import T5Tokenizer, T5ForConditionalGeneration

@click.command()
@click.argument("source_contract", type=str)
@click.option("--prediction-file", type=str, default="predictions.txt")

def main(
    source_contract,
    prediction_file
):
        os.environ['CUDA_VISIBLE_DEVICES']='0, 1, 2, 3'
        os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
        f = open(source_contract, "r")
        file = f.read()
        #pre_trained model files saved on dropbox 
        model = T5ForConditionalGeneration.from_pretrained("https://www.dropbox.com/home/content/outputs/model_files") #https://www.dropbox.com/scl/fo/jam9hpy3vuz8lyjsuh9ao/h?dl=0&rlkey=ap18dh15tkqijaea33qmywyvo")
        tokenizer = T5Tokenizer.from_pretrained("t5-small")
        col = ['Test']
        df = pd.DataFrame([file], columns=col)

        model.eval()
        test_val = TestDataSetClass(df, tokenizer, source_len=512, source_text="Test")
        test_loader = DataLoader(test_val, **test_params)
        predictions = []
        with torch.no_grad():
                for _, data in enumerate(test_loader, 0):
                        ids = data['source_ids']
                        mask = data['source_mask'].to(device, dtype = torch.long)

                        generated_ids = model.generate(
                        input_ids = ids,
                        attention_mask = mask, 
                        max_length=150, 
                        num_beams=2,
                        repetition_penalty=2.5, 
                        length_penalty=1.0, 
                        early_stopping=True
                        )
                        preds = [tokenizer.decode(g, skip_special_tokens=True, \
                                                clean_up_tokenization_spaces=True) for g in generated_ids]
                        print("preds: ", preds)
                        if _%10==0:
                                console.print(f'Completed {_}')
                        predictions.extend(preds)

        with open(prediction_file, 'w') as outfile:
                prediction_file.write(predictions)
        file.close()
        prediction_file.close()
if __name__ == "__main__":
   # A little disconcerting, but click injects the arguments for you.
    main()