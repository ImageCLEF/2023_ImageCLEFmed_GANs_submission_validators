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

- In order to use the validator you have to execute the script `validator.py` in the folder `task1`
- Please make sure that your current working directory is `task1`, otherwise errors will show up
- Provide a submission file path as the only argument to `validator.py`

*Example*:
```bash
cd ./task1
python3 ./validator.py ./test_runs/00_1_OK.csv
```

#### Unit tests (optional)

In case you want to execute the unit tests, change your current working directory to `./task1/test_runs` and execute `python3 test.py`.
All unit tests should pass. You can find more information in `README.md` in `./task1/test_runs`.