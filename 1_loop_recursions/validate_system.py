from pathlib import Path
from datetime import datetime

class ValidateSystem:
    def __init__(self, function_object, path_to_test_data: Path):
        """ Runs validation through test files

        Examples:
            >>> from character_counter import CharacterCounter
            >>> ValidateSystem(CharacterCounter.count_character_with_loop, TEST_DATA_PATH)
            Testing function name: count_character_with_loop
            ------------------------------------------------------------------------------------------------
            Task     | Result   | Answer   | Status   | File_Task       | File_Answer     | Duration        |
            ------------------------------------------------------------------------------------------------
            12345678 | 8        | 8        | True     | test.0.in       | test.0.out      | 0:00:00.000003  |
            ------------------------------------------------------------------------------------------------
            123456.. | 64       | 64       | True     | test.1.in       | test.1.out      | 0:00:00.000004  |
            ------------------------------------------------------------------------------------------------
                     | 0        | 0        | True     | test.2.in       | test.2.out      | 0:00:00.000002  |
            ------------------------------------------------------------------------------------------------
            $        | 1        | 1        | True     | test.3.in       | test.3.out      | 0:00:00.000002  |
            ------------------------------------------------------------------------------------------------
            abcdef.. | 25       | 26       | False    | test.4.in       | test.4.out      | 0:00:00.000002  |
            ================================================================================================
            Result: FAIL	 total time: 0:00:00.000728
            <validate_system.ValidateSystem object at 0x7f93380d8e20>
        """
        self.result = self.test_this_function(function_object, path_to_test_data)

    def test_this_function(self, function, test_data_directory: Path) -> bool:
        """ Validate if result from input function is the same as from answer file '.out' for task from file '.in' """
        print(f"Testing function name: {function.__name__}")
        test_start = datetime.now()
        final_status = []
        statistic = []
        task_files = sorted(test_data_directory.glob('*.in'))
        # loop for all files with test data from test_data_directory
        for task_file in task_files:
            task = task_file.read_text()
            task = task.replace('\n', '')

            # run given function with task from task_file
            start = datetime.now()
            function_result = function(task)
            stop = datetime.now()

            # search answer_file as task_file name
            answer_file_name = task_file.name.replace('in', 'out')
            answer_file = list(test_data_directory.glob(answer_file_name))[0]
            answer = answer_file.read_text()
            answer = answer.replace('\n', '')

            status = False
            if function_result == answer:
                status = True
            final_status.append(status)
            statistic.append([task, function_result, answer, str(status), task_file.name, answer_file.name, str(stop-start)])

        self.print_report(statistic)
        test_stop = datetime.now()
        if False in final_status:
            print(f"Result: FAIL\t total time: {str(test_stop-test_start)}")
            return False
        else:
            print(f"Result: SUCCESS\t total time: {str(test_stop-test_start)}")
            return True

    @staticmethod
    def print_report(values: list) -> None:
        """ Prints all statistic from tests """
        print('-' * 96)
        print('{:8} | {:8} | {:8} | {:8} | {:15} | {:15} | {:15} |'.
              format('Task', 'Result', 'Answer', 'Status', 'File_Task', 'File_Answer', "Duration"))
        for value in values:
            for index in range(4):
                if len(value[index]) > 8:
                    value[index] = value[index][:6]+'..'
        for line in values:
            print('-'*96)
            print('{:8} | {:8} | {:8} | {:8} | {:15} | {:15} | {:15} |'.format(*line))
        print("="*96)


if __name__ == '__main__':
    pass
