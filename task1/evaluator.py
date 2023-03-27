import csv
import sys
import os


class ImageCLEFGansTask1Validator:
    def __init__(self, image_ids_file_path):
        self.image_ids_file_path = image_ids_file_path
        self.load_image_ids();

    def load_image_ids(self):
        with open(self.image_ids_file_path) as file:
            self.image_ids = [line.rstrip() for line in file]

    def validate_format(self, submission_file_path):
        print("validating format...")
        
        with open(submission_file_path) as csv_file:
            reader = csv.reader(csv_file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
            line_nbr = 0
            predictions = {}

            for row in reader:
                line_nbr += 1

                if len(row) != 2:
                    self.raise_exception("Wrong format: Each line must consist of 2 tokens separated by a comma. You have to specify a figure ID "
                                            + "followed by a score of 0 or 1 to indicates whether the image was used for training or not (0=not used, 1=used). "
                                            + "Each token must be separated by a comma ({}).", line_nbr, "<figure_id>, <0 | 1>")

                image_id = row[0]

                if image_id not in self.image_ids:
                    self.raise_exception("Figure ID '{}' is not contained in testset.", line_nbr, image_id)

                if image_id in predictions:
                    self.raise_exception("Figure ID '{}' was specified more than once in submission file.", line_nbr, image_id)         
                    
                score = row[1]
                
                try:
                    score = int(score)
                    print(score)
                    if score != 0 and score !=1:
                        raise ValueError
                except ValueError:
                    self.raise_exception("Score '{}' must be either 0 or 1 (0=not used for training, 1=used for training).", line_nbr, score)

                predictions[image_id] = score


            if len(predictions) != len(self.image_ids):
                self.raise_exception("Number of figure IDs in submission file not equal to number of figure IDs in testset.", line_nbr)



    def raise_exception(self, message, line_nbr, *args):
        raise Exception(message.format(*args) +
                        " Error occured at line nbr {}.".format(line_nbr))




if __name__ == "__main__":

    usage_message = "Usage: evaluator.py submission_file_path"

    if len(sys.argv) != 2 or (len(sys.argv) == 2 and str(sys.argv[1]) == '--help'):
       print(usage_message)
       sys.exit()

    submission_file_path = str(sys.argv[1])

    if not os.path.isfile(submission_file_path):
        print("{} is not an existing file".format(submission_file_path))
        sys.exit()

    image_ids_file_path = "./image_ids"
    

    imageCLEFGansTask1Validator = ImageCLEFGansTask1Validator(image_ids_file_path)
    imageCLEFGansTask1Validator.validate_format(submission_file_path)
