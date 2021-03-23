import os
import logging
import mandrill
import argparse

log = logging.getLogger(__name__)


class MandrillOperations(object):
    def __init__(self, mandrill_key):
        self.mandrill_client = mandrill.Mandrill(mandrill_key)
        self.dist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dist'))

    def update_template(self, name, from_email, from_name = '', labels = [], subject = 'template update', text = '', publish = True, template_file_name='anomalyAlert.html'):
        """
            {'code': '<div mc:edit="editable">editable content</div>',
             'created_at': '2013-01-01 15:30:27',
             'from_email': 'from.email@example.com',
             'from_name': 'Example Name',
             'labels': ['example-label'],
             'name': 'Example Template',
             'publish_code': '<div mc:edit="editable">different than draft content</div>',
             'publish_from_email': 'from.email.published@example.com',
             'publish_from_name': 'Example Published Name',
             'publish_name': 'Example Template',
             'publish_subject': 'example publish_subject',
             'publish_text': 'Example published text',
             'published_at': '2013-01-01 15:30:40',
             'slug': 'example-template',
             'subject': 'example subject',
             'text': 'Example text',
             'updated_at': '2013-01-01 15:30:49'}
        """

        template_path = os.path.join(self.dist_path, template_file_name)
        if os.path.exists(template_path):
            with open(template_path, 'r') as file:
                content = file.read()
        else:
            raise FileNotFoundError('path "{template_path}" does not exists!'.format(
                template_path=template_path))

        try:
            return self.mandrill_client.templates.update(name=name,
                                                         from_email=from_email,
                                                         from_name=from_name,
                                                         subject=subject,
                                                         code=content,
                                                         text=text,
                                                         publish=publish,
                                                         labels=labels)

        except mandrill.Error as e:
            # Mandrill errors are thrown as exceptions
            # Ex - A mandrill error occurred: <class 'mandrill.InvalidKeyError'> - Invalid API key
            log.exception('A mandrill error occurred: {error_class} - {error}'.format(
                error_class=e.__class__, error=e))

            raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-k', '--key',
        type=str,
        required=True
    )

    parser.add_argument(
        '-o', '--operation',
        type=str,
        choices=['update'],
        required=True
    )

    parser.add_argument(
        '-e', '--email',
        help='your email id',
        type=str,
        required=True
    )

    parser.add_argument(
        '-t', '--template_name',
        type=str,
        required=True
    )

    parser.add_argument(
        '-f', '--file_name',
        type=str,
        required=True
    )

    args = parser.parse_args()

    operations = MandrillOperations(args.key)

    if args.operation == 'update':
        result = operations.update_template(name=args.template_name,
                                            from_email=args.email,
                                            template_file_name=args.file_name)
        log.info('{}'.format(result))
