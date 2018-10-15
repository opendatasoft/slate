#env python
import csv
import sys

PERMISSIONS_LIST = ["EDIT_DOMAIN", "EDIT_PAGE", "EDIT_DATASET", "PUBLISH_DATASET",
                    "MANAGE_DATASET", "CREATE_DATASET", "EDIT_REUSE", "MANAGE_SUBDOMAINS",
                    "EDIT_THEME", "CREATE_PAGE", "MANAGE_PAGE", "EXPLORE_RESTRICTED_DATASET",
                    "EXPLORE_PUBLIC_DATASET", "EXPLORE_MONITORING", "EXPLORE_RESTRICTED_PAGE"]

def format_permissions(permissions):
    for perm in PERMISSIONS_LIST:
        permissions = permissions.replace(perm, '`{}`'.format(perm.lower()))
    return permissions

if len(sys.argv) != 2:
    print 'Usage: {} <permissions_csv_file>'.format(sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()  # Skip header

    for row in reader:
        if not row[3] and not row[4] and not row[5]:
            continue

        print '### {}\n'.format(row[0])
        print '`{} /api/management/v2{}`\n'.format(row[2], row[1])

        required = []


        if row[3]:
            required.append('domain permission: {}'.format(format_permissions(row[3])))

        if row[4]:
            required.append('any dataset permission: {}'.format(format_permissions(row[4])))

        if row[5]:
            required.append('current dataset permission: {}'.format(format_permissions(row[5])))

        if len(required) == 1:
            print 'Requires {}'.format(required[0])
        else:
            print 'Requires one of the following:\n'
            for req in required:
                print '- {}'.format(req)

        print ''
