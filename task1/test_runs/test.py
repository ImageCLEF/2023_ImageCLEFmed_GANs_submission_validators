import unittest
import sys
sys.path.append('..')
from evaluator import ImageCLEFGansTask1Validator
from evaluator import SubmissionValidationException

image_ids_file_path = "../resources/image_ids.txt"

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.imageCLEFGansTask1Validator = ImageCLEFGansTask1Validator(image_ids_file_path)


    
    def test_valid_file_1(self):
        # Should not raise any exception
        self.imageCLEFGansTask1Validator.validate_format("./00_1_OK.csv")

    def test_valid_file_2(self):
        # Should not raise any exception
        self.imageCLEFGansTask1Validator.validate_format("./00_2_OK.csv")

    def test_wrong_format_1(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Wrong format", self.imageCLEFGansTask1Validator.validate_format, "01_1_empty_line.csv")

    def test_wrong_format_2(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Wrong format", self.imageCLEFGansTask1Validator.validate_format, "01_2_wrong_format.csv")
    
    def test_wrong_figure_id(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Figure ID 'aaaaaaaa' is not contained in testset.", 
                               self.imageCLEFGansTask1Validator.validate_format, "02_1_wrong_figure_id.csv")
    
    def test_same_figure_id_more_than_once(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Figure ID 'real_unknown_0090' was specified more than once in submission file.", 
                               self.imageCLEFGansTask1Validator.validate_format, "03_1_same_fig_id_more_than_once.csv")
        
    def test_wrong_score_1(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Wrong score 'aaaaaaa'.", self.imageCLEFGansTask1Validator.validate_format, "04_1_score_no_int.csv")

    def test_wrong_score_2(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Wrong score '2'.", self.imageCLEFGansTask1Validator.validate_format, "04_2_score_int_greater_than_1.csv")

    def test_wrong_score_3(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Wrong score '-1'.", self.imageCLEFGansTask1Validator.validate_format, "04_3_score_int_smaller_than_0.csv")


    
    def test_not_all_figure_ids_specified(self):
        self.assertRaisesRegex(SubmissionValidationException, "^Number of figure IDs in submission file not equal to number of figure IDs in testset.", 
                               self.imageCLEFGansTask1Validator.validate_format, "05_1_not_all_fig_ids_specified.csv")



if __name__ == '__main__':
    unittest.main()