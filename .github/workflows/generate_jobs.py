import argparse
import json
from pathlib import Path


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('changes', nargs='?')
    args = parser.parse_args()
    return args


def main():
    args = get_arguments()
    try:
        changes_list = args.changes.split(',')
    except AttributeError:
        changes_list = None

    try:
        if changes_list is None:
            pass
        else:
            matrix = {'include': []}
            for changed_file in changes_list:
                application = Path(changed_file).parts[1]

                application_matrix_exists = False
                for application_matrix in matrix['include']:

                    if application_matrix['application'] == application:
                        application_matrix_exists = True
                        break

                if not application_matrix_exists:
                    matrix['include'].append(
                        {'application': application})

            print(json.dumps(matrix))

    except Exception as e:
        print(e)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
