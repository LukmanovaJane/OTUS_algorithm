from pathlib import Path


def test_this_function(function, test_data_directory: Path) -> bool:
    """ Validate if result from input function is the same as from answer file '.out' for task from file '.in'

    Examples:
        >>> test_this_function(count_characters, TEST_DATA_PATH)
        Task     | Result   | Answer   | Status   | File_Task       | File_Answer     |
        -------------------------------------------------------------------------------
        $        | 1        | 1        | True     | test.3.in       | test.3.out      |
        -------------------------------------------------------------------------------
        12345678 | 64       | 64       | True     | test.1.in       | test.1.out      |
        -------------------------------------------------------------------------------
        abcdefgh | 25       | 26       | False    | test.4.in       | test.4.out      |
        -------------------------------------------------------------------------------
        12345678 | 8        | 8        | True     | test.0.in       | test.0.out      |
        -------------------------------------------------------------------------------
                 | 0        | 0        | True     | test.2.in       | test.2.out      |
        ===============================================================================
        Result: FAIL
        False
    """
    print('{:8} | {:8} | {:8} | {:8} | {:15} | {:15} |'.format('Task', 'Result', 'Answer', 'Status', 'File_Task', 'File_Answer'))
    final_status = []
    task_files = test_data_directory.glob('*.in')
    # loop for all files with test data from test_data_directory
    for task_file in task_files:
        task = task_file.read_text()
        task = task.replace('\n', '')

        function_result = function(task)

        answer_file_name = task_file.name.replace('in', 'out')
        answer_file = list(test_data_directory.glob(answer_file_name))[0]
        answer = answer_file.read_text()
        answer = answer.replace('\n', '')

        status = False
        if function_result == answer:
            status = True
        final_status.append(status)

        print('-'*79)
        print('{:8} | {:8} | {:8} | {:8} | {:15} | {:15} |'.format(
            f'{task[0:8]}', function_result, answer, str(status), task_file.name, answer_file.name)
        )
    print("="*79)
    if False in final_status:
        print(f"Result: FAIL")
        return False
    else:
        print(f"Result: SUCCESS")
        return True


def count_characters(string: str) -> str:
    """ Count characters in given string

    Examples:
        >>> count_characters('abcdefghijklmnoprstuvwxyz')
        '25'
    """
    counter = 0
    for char in string:
        counter += 1
    return str(counter)


if __name__ == '__main__':
    pass
