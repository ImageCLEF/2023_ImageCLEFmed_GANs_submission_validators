# 2023_ImageCLEFmed_GANs_submission_validators

## Task 1

### Format

The submission format is the following `<figure_id>,<score>` where ...
- figure_id is a line contained in `./resources/image_ids.txt`
- comma (`,`) is the delimiter
- score is a number that indicates whether the image was used for training or not (0 = not used and 1 = used)


### Run task 1 submission format validator

#### Requirements
Please make sure you are using Python 3.2 or above.

#### Usage

- In order to use the validator you have to execute the script `evaluator.py` in the folder `task1`
- Please make sure that your current working directory is `task1`, otherwise errors will show up
- Provide a submission file path as the only argument to `evaluator.py`

*Example*:
```bash
cd ./task1
python3 ./evaluator.py ./test_runs/00_1_OK.csv
```