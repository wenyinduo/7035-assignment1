import pandas as pd


def clean(contact_info_file, other_info_file):
    left = pd.read_csv(contact_info_file)
    right = pd.read_csv(other_info_file)
    data_merge = pd.merge(left, right, left_on='respondent_id', right_on='id', how='left')
    data_clean = data_merge.dropna()
    data_clean = data_clean[~ data_clean['job'].str.contains('Insurance|insurance')]
    data_clean = data_clean.drop('id', axis=1)
    return data_clean


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('other_info_file', help='Data file (CSV)')
    parser.add_argument('contact_info_file', help='Data file (CSV)')
    parser.add_argument('output_file', help='Cleaned data file (CSV)')

    args = parser.parse_args()

    cleaned = clean(args.other_info_file, args.contact_info_file)
    cleaned.to_csv(args.output_file, index=False)





