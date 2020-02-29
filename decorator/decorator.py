# coding: utf8


def make_bold(func):
	def wrapper():
		return "<b>%s</b>" % func()

	return wrapper


@make_bold
def get_bold_content():
	return 'content'


def make_header(level):
	def decorator(func):
		def wrapper():
			return "<h{0}>{1}</h{0}>".format(level, func())

		return wrapper

	return decorator


@make_header(1)
def get_header_content():
	return "content"


if __name__ == '__main__':
	print get_bold_content
	print get_header_content
