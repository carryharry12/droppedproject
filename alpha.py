

import sys
import importlib
"""
class auto_module:

	def __init__(self):
		self.__MODULES__ = [
			'pywinauto',
			'psutil',
			'requests',
			'colorama',
			'dnspython',
			'schedule',
			'winreg',
			'python-dateutil',
			'cryptography']
		
		self._MODULES_NAMES = [
			'pywinauto',
			'psutil',
			'requests',
			'colorama',
			'dns',
			'schedule',
			'winreg',
			'dateutil',
			'cryptography']


	def auto_os(self, os_p):

		try:
			os.system('pip install {}'.format(os_p))
		except Exception:
			e = None

			try:
				print(str(e))
			finally:
				e = None
				del e




	def check_modules(self):

		try:
			success = 0

			try:
				importlib.import_module(self._MODULES_NAMES[0])
				success += 1
			except:
				self.auto_os(self.__MODULES__[0])


			try:
				importlib.import_module(self._MODULES_NAMES[1])
				success += 1
			except:
				self.auto_os(self.__MODULES__[1])


			try:
				importlib.import_module(self._MODULES_NAMES[2])
				success += 1
			except:
				self.auto_os(self.__MODULES__[2])


			try:
				importlib.import_module(self._MODULES_NAMES[3])
				success += 1
			except:
				self.auto_os(self.__MODULES__[3])


			try:
				if platform.system() == 'Windows':
					importlib.import_module(self._MODULES_NAMES[4])
					success += 1
			except:
				self.auto_os(self.__MODULES__[4])


			try:
				importlib.import_module(self._MODULES_NAMES[5])
				success += 1
			except:
				self.auto_os(self.__MODULES__[5])


			try:
				importlib.import_module(self._MODULES_NAMES[6])
				success += 1
			except:
				self.auto_os(self.__MODULES__[6])


			try:
				importlib.import_module(self._MODULES_NAMES[7])
				success += 1
			except:
				self.auto_os(self.__MODULES__[7])

			if success >= 6:
				return 1
			return None
		except Exception:
			e = None

			try:
				print(str(e))
			finally:
				e = None
				del e


"""


try:
	from multiprocessing.dummy import Pool as ThreadPool
	import os
	import dns.resolver as dns
	import platform
	import psutil
	from json import loads
	from pywinauto import Desktop, Application
	from html import unescape
	from requests import post, get
	from socket import gethostname
	from uuid import uuid1
	from string import hexdigits, digits, ascii_uppercase, ascii_lowercase
	from random import choice
	from re import findall, search
	from base64 import b64encode
	from hashlib import sha256
	from smtplib import SMTP, SMTP_SSL
	from uuid import getnode as get_mac
	from email.utils import formataddr, make_msgid, formatdate
	from email.charset import CHARSETS
	from time import sleep
	from email.mime.application import MIMEApplication
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from datetime import datetime, timedelta
	from colorama import Fore, Style
	import email.mime as email
	import email.mime.nonmultipart as email
	import email.charset as email
except Exception:
	e = None
	"""
	try:
		print(str(e))
		auto_module().check_modules()
		#sys.exit()
	finally:
		e = None
		del e
	"""



class Anonym_Sender:

	def __init__(self):
		self.api = 'https://raw.githubusercontent.com/urie2021/activation/main/server.txt'
		self.api_manage = self.get_data()
		self.headers_path = './configs/headers.json'
		self.config_path = './configs/config.json'
		self.debug_path = './configs/debug.json'
		self.save_log_path = './internal_files/log.json'
		self.timer_path = './internal_files/timer.json'
		self.country_path = './internal_files/country.json'
		self.os_path = './internal_files/os.json'
		self.browser_path = './internal_files/browser.json'
		self.mailist_file_name = 'files/mailist.txt'
		self.smtp = 'files/smtp.txt'
		self.letter = 'files/letter.html'
		self.random_keys = [
			'random_number',
			'email_user',
			'link_unsubscribe',
			'random_md5',
			'time_now',
			'random_os',
			'random_ip',
			'random_country',
			'random_browser',
			'link_rotation',
			'email']
		self.timeout = 25
		self.red = Fore.RED
		self.cyan = Fore.CYAN
		self.magenta = Fore.MAGENTA
		self.white = Fore.WHITE
		self.yellow = Fore.YELLOW
		self.blue = Fore.BLUE
		self.green = Fore.GREEN
		self.reset = Fore.RESET
		self.normal = Style.NORMAL
		self.bright = Style.BRIGHT
		self.reset = Fore.RESET
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate, br',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			'Sec-Fetch-Dest': 'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site': 'none',
			'Sec-Fetch-User': '?1' }
		self.mailist_reference = 0
		self.message_id = False
		self.auto_crypt = False
		self.code_exception = None
		self.translate = False
		self.vpn_data = { }
		self.vpn_counter = 1
		self.bcc = 0
		self.bcc_counter = 1
		self.alpha_logo = 'https://pastebin.com/raw/X9cfsmWC'


	def get_mac(self):
		mac = get_mac()
		data = ':'.join((('%012X' % mac)[i:i + 2] for i in range(0, 12, 2)))
		return data

	def get_data(self):
		try:
			headers = {
			 'User-Agent': "'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'",
			 'Accept': "'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'",
			 'Accept-Language': "'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3'",
			 'Accept-Encoding': "'gzip, deflate, br'",
			 'Connection': "'keep-alive'",
			 'Upgrade-Insecure-Requests': "'1'",
			 'Sec-Fetch-Dest': "'document'",
			 'Sec-Fetch-Mode': "'navigate'",
			 'Sec-Fetch-Site': "'none'",
			 'Sec-Fetch-User': "'?1'"}
			#d = get((self.api), headers=headers)
			#return d.text
			return 1
		except Exception as e:
			try:
				pass
			finally:
				e = None
				del e

	def open_now(self, filename, permission):
		try:
			op = open(filename, permission, encoding='utf-8')
			return op.read()
		except:
			try:
				op = open(filename, permission, encoding='unicode_escape')
				return op.read()
			except Exception as e:
				try:
					if self.debug_read()[2]:
						print(str(e))
				finally:
					e = None
					del e
					
	def debug_read(self):
		try:
			debug_file = self.open_now(self.debug_path, 'r')
			json_debug = loads(debug_file)
			return [
			 json_debug['smtp_debug'], json_debug['bounce_debug'], json_debug['error_script']]
		except Exception as e:
			try:
				return [
				 False, False, False]
			finally:
				e = None
				del e

	def generate_ip(self):
		try:
			first_range = str(choice(range(1, 255)))
			second_range = str(choice(range(0, 266)))
			third_range = str(choice(range(0, 266)))
			fourth_range = str(choice(range(0, 266)))
			return '{}.{}.{}.{}'.format(first_range, second_range, third_range, fourth_range)
		except Exception as e:
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e

	def find_keys_forbidden(self, key):
		try:
			if key.count('#') == 4:
				return 0
			return 1
		except Exception as e:
			try:
				return 1
			finally:
				e = None
				del e

	def auto_translate(self, file_up, lang, lang_to):
		try:
			if lang:
				if lang_to:
					if not file_up or len(lang) != 2 or len(lang_to) != 2:
						return file_up
				lang = lang.lower()
				lang_to = lang_to.lower()
				headers = {
				  'sec-ch-ua-mobile': '?0',
				  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
				  'Content-Type': 'application/json',
				  'Accept': '*/*',
				  'Origin': 'https://libretranslate.com',
				  'Sec-Fetch-Site': 'same-origin',
				  'Sec-Fetch-Mode': 'cors',
				  'Sec-Fetch-Dest': 'empty',
				  'Referer': 'https://libretranslate.com/?source=auto&target=es&q=hello',
				  'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
				  'Cookie': '_ga=GA1.1.106380441.1671231923; _ga_KPKM1EP5EW=GS1.1.1671231923.1.1.1671232123.0.0.0'}
				file_sources = file_up.replace('\t', '').replace('\n', '').replace('&#39;', "'")
				file_source = crypto().unescape(file_sources)
				try:
					file_source = file_sources.split('<body')[1]
				except:
					try:
						file_source = file_sources.split('</head')[1]
					except:
						file_source = file_sources

				keys_data = findall('>(.*?)<', file_source)
				translated = {}
				t = 1
				for keys in keys_data:
					if len(keys) > 1:
						if self.find_keys_forbidden(keys) == 1:
							if 'amp' not in keys:
								if 'nbsp' not in keys:
									if '@' not in keys:
										data_to = {
										  'q': keys,
										  'source': lang_to,
										  'target': lang,
										  'format': 'text',
										  'api_key': ''}
										r = post('https://libretranslate.com/translate', headers=headers, json=data_to)
										try:
											trans = loads(r.text)['translatedText']
										except:
											sleep(60)

										timer = self.yellow + 'Translating Now ... Total Sentences : {:02d} '.format(t)
										t += 1
										print(timer, end='\r')
										translated[keys] = trans

			print('\n')
			file_source = crypto().replace_all(file_sources, translated)
			return crypto().unescape(file_source)
		except Exception as e:
			try:
				print(str(e))
				return file_up
			finally:
				e = None
				del e

	def base64_encode(self, sample_string):
		try:
			if self.base64encode:
				sample_string_bytes = sample_string.encode('utf-8')
				base64_bytes = b64encode(sample_string_bytes)
				base64_string = base64_bytes.decode('utf-8')
				new_text = '=?UTF-8?B?{}=?='.format(base64_string)
				return new_text
			return sample_string
		except Exception as e:
			try:
				return sample_string
			finally:
				e = None
				del e

	def str_replace(self, letter, email_user_to, user):
		try:
			try:
				key = findall('##(.*?)##', letter)
			except:
				return letter
			else:
				for keys in key:
					full_hashtag = '##{}##'.format(keys)
					if 'random_number' in keys:
						set_number = keys.split('random_number_')[1]
						letter = letter.replace(full_hashtag, mix_random().random_data(int(set_number), 'digits'))
					else:
						if 'random_md5' in keys:
							crypto = sha256(str(mix_random().random_data(8, 'digits')).encode('utf-8'))
							letter = letter.replace(full_hashtag, str(crypto.hexdigest()))
						else:
							if 'email_user' in keys:
								letter = letter.replace(full_hashtag, email_user_to.split('@')[0])
							else:
								if 'time_now' in keys:
									letter = letter.replace(full_hashtag, formatdate())
								else:
									if 'random_os' in keys:
										letter = letter.replace(full_hashtag, choice(random_o().random_os))
									else:
										if 'random_ip' in keys:
											letter = letter.replace(full_hashtag, self.generate_ip())
										else:
											if 'link_unsubscribe' in keys:
												letter = letter.replace(full_hashtag, management_newsletters().unsubscribe_link_generator(user, email_user_to))
											else:
												if 'random_country' in keys:
													letter = letter.replace(full_hashtag, choice(random_o().random_country))
												else:
													if 'random_browser' in keys:
														letter = letter.replace(full_hashtag, choice(random_o().random_browser))
					if 'email' in keys:
						letter = letter.replace(full_hashtag, email_user_to)

			return letter
		except Exception as e:
			try:
				if self.debug_read()[2]:
					print(str(e))
				return letter
			finally:
				e = None
				del e

	def time_counter(self):
		try:
			time = datetime.now()
			hour = int(time.strftime('%H'))
			minute = int(time.strftime('%M'))
			second = int(time.strftime('%S'))
			req = open(self.timer_path, 'w+')
			formats = '{"hour" : ' + str(hour) + ', "minute" : ' + str(minute) + ',"second":' + str(second) + '}'
			req.write(formats)
		except Exception as e:
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e

	def array_in_file(self, array, filo):
		for arr in array:
			if arr in filo:
				return 1

		return 0

	def headers_split(self):
		try:
			file_open = loads(self.open_now(self.headers_path, 'r'))
			array_r = {}
			for key in file_open:
				array_r[key] = self.str_replace(file_open[key], '', None)

			return array_r
		except Exception as e:
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e

	def remove_dpl_list(self, list_array):
		if self.remove_dupl:
			list_dpl = []
			for email in list_array:
				if email not in list_dpl:
					list_dpl.append(email)

			return list_dpl
		return list_array

	def run_vpn(self):
		script_name = 'Vpn'
		connected = False
		timeout_connexion = int(self.vpn_data['timeout_connexion'])
		for proc in psutil.process_iter(['name']):
			if proc.info['name'] == f"{script_name}.exe":
				try:
					vpn_app = Application(backend='uia').start(self.vpn_data['path_vpn'])
					dialog = Desktop(backend='uia').HMA
					panel0 = dialog.Pane
					connect_button = panel0.ConnectButton
					changeIP = panel0.Button5
					if connect_button.get_toggle_state():
						changeIP.click()
					else:
						connect_button.click()
					print(self.green + '\n[VPN CHANGE]' + self.white + ' Please Wait {} Seconds ... \n'.format(str(timeout_connexion)))
					connected = True
				except:
					print(self.cyan + '\n[VPN NOT CHANGED]' + self.white + ' Please Wait {} Seconds ... \n'.format(str(timeout_connexion)))

				break

		if not connected:
			print(self.red + '\n[VPN NOT FOUND]' + self.white + ' Please Wait {} Seconds ... \n'.format(str(timeout_connexion)))
			self.vpn_data['activation'] = False
		sleep(timeout_connexion)

	def auto_email_send(self):
		try:
			self.letter = self.open_now(self.letter, 'r')
			data_headers = self.headers_split()
			try:
				if not self.negative_file:
					if os.path.isfile(self.negative_file) and os.path.getsize(self.negative_file) > 10:
						try:
							negative_file = self.open_now(self.negative_file, 'r')
							self.letter += negative_file
						except:
							self.letter = self.letter

			except:
				pass

			if self.translate['activation']:
				self.letter = self.auto_translate(self.letter, self.translate['lang_to'], self.translate['lang_from'])
			smtp_files = self.open_now(self.smtp, 'r')
			open_smtp = smtp_files.split('\n')
			count_smtp = len(open_smtp)
			mailist_files = self.open_now(self.mailist_file_name, 'r')
			self.open_mailist = self.remove_dpl_list(mailist_files.split('\n'))
			count_maillist = len(self.open_mailist)
			smtp_line_reference = 0
			counter = 0
			email_test_counter = 1
			sleep_after_sending_emails_counter = 1
			link_rotation_counter = 1
			link_rotation_array = 0
			failed_row_counter = 0
			email_check = False
			if self.rotation['activation']:
				if count_smtp > 1:
					self.time_counter()
			self.read_log()
			if self.Charset == 'quoted-printable':
				CHARSETS[self.Content_Encoding] = (
				 3, 1, self.Content_Encoding)
			msg = MIMEMultipart()
			if os.path.isfile(self.attachment_file_name):
				try:
					if os.path.getsize(self.attachment_file_name) > 10:
						files_open = open(self.attachment_file_name, 'rb')
						basename = os.path.basename(self.attachment_file_name)
						part = MIMEApplication((files_open.read()), Name=basename)
						part['Content-Disposition'] = 'attachment; filename="%s"' % basename
						msg.attach(part)
				except Exception as e:
					print(str(e))
					try:
						if self.debug_read()[2]:
							print(str(e))
					finally:
						e = None
						del e

			msg['Date'] = formatdate()
			if email_regex().email_valid(self.return_path):
				msg['Return-Path'] = '<bounce+dc4675.56089b-alice=@{}>'.format(self.from_email.split('@')[1])
			if email_regex().email_valid(self.reply['to']):
				if self.reply['name']:
					msg['Reply-to'] = '{} <{}>'.format(self.reply['name'], self.reply['to'])
			if self.X_Priority > 0:
				msg['X-Priority'] = str(self.X_Priority)
			if len(data_headers) >= 1:
				for headers in data_headers:
					if headers not in msg:
						msg[headers] = self.str_replace(data_headers[headers], self.open_mailist[self.mailist_reference].strip(), email_login)

			while smtp_line_reference < count_smtp and self.mailist_reference < count_maillist:
				del msg['From']
				try:
					if smtp_line_reference < count_smtp:
						smtp_config = open_smtp[smtp_line_reference].strip().split(':')
						host_mx = smtp_config[0].strip()
						try:
							self_port = int(smtp_config[1].strip())
						except Exception as e:
							print(str(e))
							try:
								smtp_line_reference += 1
								continue
							finally:
								e = None
								del e

						ssl_verification = int(smtp_config[2].strip())
						email_login = smtp_config[3].strip()
						password_login = smtp_config[4].strip()
						if email_regex().email_valid(email_login) and len(smtp_config) == 5:
							self.from_email = email_login.strip()
						else:
							self.from_email = smtp_config[5].strip()
						print(self.blue + '\n Sending With : ' + self.white + self.from_email + '\n' + self.reset)
					else:
						break
					server = self.self_connect(host_mx, self_port, ssl_verification, email_login, password_login)
					if self.message_id:
						msg['Message-ID'] = make_msgid(None, host_mx)
				except Exception as e:
					print(str(e))
					try:
						if self.debug_read()[2]:
							print(str(e))
						else:
							self.code_exception = smtplib_exceptions().raise_verify(str(e))
							if self.code_exception == 104:
								self.code_exception = None
								print(self.magenta + '[Change TLS Method] ++' + self.yellow + ' => ' + self.white + host_mx + self.reset + '\n')
								if self.rotation['activation'] and count_smtp > 1:
									if smtp_line_reference + 1 == count_smtp:
										self.time_calculate()
										self.time_counter()
										smtp_line_reference = 0
										continue
									else:
										smtp_line_reference += 1
										continue
								else:
									#sys.exit()
									pass
							if self.code_exception in (535, 503, 111, 101, -2, 10061,11001, 10054, 421):
								self.code_exception = None
								print(self.red + '[Login Failed]' + self.yellow + ' :=<> ' + self.white + email_login + self.reset)
								if self.rotation['activation'] and count_smtp > 1:
									if smtp_line_reference + 1 == count_smtp:
										self.time_calculate()
										self.time_counter()
										smtp_line_reference = 0
										continue
									else:
										smtp_line_reference += 1
										continue
								else:
									pass
									#sys.exit()
					finally:
						e = None
						del e

				while self.mailist_reference < count_maillist:
					if not email_regex().email_valid(self.open_mailist[self.mailist_reference].strip()):
						self.mailist_reference = self.mailist_reference + 1
					if self.link_rotation['activation']:
						data_replace = '##{}##'.format(self.random_keys[9])
						if data_replace in self.letter or self.array_in_file(self.link_rotation['links'], self.letter):
							if not len(self.link_rotation['links']) > 1 or link_rotation_counter == self.link_rotation['after_emails'] or self.mailist_reference == 0:
								if link_rotation_array == len(self.link_rotation['links']):
									link_rotation_array = 0
								elif self.mailist_reference == 0 and link_rotation_array == 0:
									self.letter = self.letter.replace(data_replace, self.link_rotation['links'][link_rotation_array])
								else:
									if self.mailist_reference > 0:
										if len(self.link_rotation['links']) > 1:
											self.letter = self.letter.replace(self.link_rotation['links'][link_rotation_array - 1], self.link_rotation['links'][link_rotation_array])
										print(self.green + '\n[LINK CHANGED] ++' + self.yellow + ' TO => ' + self.white + self.link_rotation['links'][link_rotation_array] + '\n')
										link_rotation_array += 1
										link_rotation_counter = 1
									else:
										link_rotation_counter += 1
							if self.unsubscribe_link and 'unsubscribe' not in self.letter:
								if self.Content_Type == 'html':
									self.letter = self.letter.replace('</html>', '').replace('</body>', '')
									self.letter += management_newsletters().unsubscribe_add(self.from_email.split('@')[1], self.open_mailist[self.mailist_reference], 1)
						elif self.Content_Type == 'plain':
							self.letter += management_newsletters().unsubscribe_add(self.from_email.split('@')[1], self.open_mailist[self.mailist_reference], 0)
					else:
						if self.unsubscribe_link:
							data_in = management_newsletters().unsubscribe_link_generator(self.from_email.split('@')[1], self.open_mailist[self.mailist_reference].strip())
							if self.Content_Type == 'html':
								msg['List-Unsubscribe'] = '<{}>, <mailto:leave-fd8215781a3c402029@{}>'.format(data_in, self.from_email.split('@')[1], 1)
							else:
								msg['List-Unsubscribe'] = '<{}>, <mailto:leave-fd8215781a3c402029@{}>'.format(data_in, self.from_email.split('@')[1], 0)
						else:
							msg['To'] = str(self.open_mailist[self.mailist_reference].strip())
							main_letter = self.str_replace(self.letter, self.open_mailist[self.mailist_reference].strip(), self.from_email.split('@')[1])
							if self.auto_crypt:
								crypto().start_crypt()
							part1 = MIMEText(main_letter, self.Content_Type, self.Content_Encoding)
							msg.set_payload([])
							msg.attach(part1)
							msg['Subject'] = str(self.base64_encode(self.str_replace(choice(self.subject), self.open_mailist[self.mailist_reference].strip(), email_login)))
							msg['From'] = formataddr((self.base64_encode(self.str_replace(choice(self.from_name), self.open_mailist[self.mailist_reference].strip(), email_login)), str(self.from_email)))
							try:
								if self.email_bounce_validation:
									email_check = debouncer().verify(email_login, self.open_mailist[self.mailist_reference], self.debug_read()[1])
									if email_check == 3:
										server.sendmail(msg['From'], msg['To'], msg.as_string())
									cls_print().auto_print(email_check, self.mailist_reference, self.open_mailist[self.mailist_reference].strip(), self.from_email)
								else:
									server.sendmail(msg['From'], msg['To'], msg.as_string())
									cls_print().auto_print(1, self.mailist_reference, self.open_mailist[self.mailist_reference].strip(), self.from_email)
								if self.email_test['after_emails'] > 0 and email_regex().email_valid(self.email_test['email_to']) and self.email_test['after_emails'] == email_test_counter and self.email_test['email_to'] != self.open_mailist[self.mailist_reference]:
									del msg['To']
									msg['To'] = self.email_test['email_to']
									server.sendmail(msg['From'], msg['To'], msg.as_string())
									print(self.yellow + '\n[SUCCESS TEST] ++' + self.yellow + ' FROM ' + self.white + self.from_email + self.yellow + ' TO ' + self.white + self.email_test['email_to'] + '\n')
									email_test_counter = 1
								else:
									if self.email_test['after_emails'] > 0:
										email_test_counter = email_test_counter + 1 - failed_row_counter
										failed_row_counter = 0
								if self.sleep_after_sending_emails['after_email'] > 0 and self.sleep_after_sending_emails['sleep_time'] > 0 and sleep_after_sending_emails_counter == self.sleep_after_sending_emails['after_email'] and self.mailist_reference < count_maillist - 1:
									print(self.cyan + '\n[SLEEP TIME] ++' + self.yellow + ' {} Seconds '.format(str(self.sleep_after_sending_emails['sleep_time'])) + self.reset + '\n')
									sleep(int(self.sleep_after_sending_emails['sleep_time']))
									sleep_after_sending_emails_counter = 1
								else:
									if self.sleep_after_sending_emails['after_email'] > 0:
										if self.sleep_after_sending_emails['sleep_time'] > 0:
											sleep_after_sending_emails_counter = sleep_after_sending_emails_counter + 1 - failed_row_counter
											failed_row_counter = 0
									else:
										if self.sleep_time_between_emails > 0:
											if self.mailist_reference < count_maillist - 1:
												sleep(self.sleep_time_between_emails)
										if self.bcc > 0 and self.bcc_counter == self.bcc:
											server.quit()
											server = self.self_connect(host_mx, self_port, ssl_verification, email_login, password_login)
											self.bcc_counter = 0
									if self.bcc > 0:
										self.bcc_counter += 1
								if self.vpn_data['activation'] and self.vpn_data['after'] == self.vpn_counter:
									self.run_vpn()
									server = self.self_connect(host_mx, self_port, ssl_verification, email_login, password_login)
									self.vpn_counter = 1
								else:
									if self.vpn_data['activation']:
										self.vpn_counter += 1
									del msg['To']
							except Exception as e:
								print(str(e))
								try:
									if self.debug_read()[2]:
										print(str(e))
									else:
										email_test_counter += 1
										sleep_after_sending_emails_counter += 1
										self.code_exception = smtplib_exceptions().raise_verify(str(e))
										cls_print().auto_print(2, self.mailist_reference, self.open_mailist[self.mailist_reference].strip(), self.from_email)
										if self.code_exception in (501, 450, 234):
											self.mailist_reference += 1
											continue
										if self.code_exception in (251, 422, 432, 441,
																   442, 510, 511,
																   512, 513, 541):
											failed_row_counter += 1
											sleep(10)
											continue
										if self.code_exception == 421:
											print(self.magenta + '\n[RECONNEXION NOW] ++' + self.reset + '\n')
											self.mailist_reference -= 1
											self.self_connect(host_mx, self_port, ssl_verification, email_login, password_login)
											continue
										if self.code_exception in (101, 111, 446, 452,
																   553, 554, 571,
																   550, 999, 11001,
																   10061, 552):
											if self.rotation['activation'] and count_smtp > 1:
												counter = 0
												self.mailist_reference -= 1
												if smtp_line_reference + 1 == count_smtp:
													self.time_calculate()
													self.time_counter()
													smtp_line_reference = 0
												break
											else:
												#sys.exit()
												pass
									if self.code_exception in (452, 471, 500, 523,
															   535, 104, 551):
										failed_row_counter += 1
										self.mailist_reference -= 1
										self.self_connect(host_mx, self_port, ssl_verification, email_login, password_login)
										continue
								finally:
									e = None
									del e

						if self.rotation['activation']:
							if count_smtp > 1:
								if counter == self.rotation['emails_in_hour'] - 1:
									counter = 0
									server.quit()
									break
						self.mailist_reference += 1
						counter += 1

				if count_smtp > 1:
					if self.rotation['activation']:
						smtp_line_reference += 1
				self.mailist_reference += 1
				if self.rotation['activation'] and count_smtp > 1 and smtp_line_reference == count_smtp and self.mailist_reference - 1 != count_maillist:
					self.time_calculate()
					self.time_counter()
					smtp_line_reference = 0

			self.reset_log()
		except KeyboardInterrupt or Exception as e:
			try:
				if self.debug_read()[2]:
					print(str(e))
				self.show_debug_end()
			finally:
				e = None
				del e
				
	def show_debug_end(self):
		time = datetime.now()
		finish_time_two_hour = str(time.strftime('%H'))
		finish_two_minutes = str(time.strftime('%M'))
		finish_two_seconds = str(time.strftime('%S'))
		print(self.cyan + '\n  Program End In : {}{}:{}:{}'.format(self.white, finish_time_two_hour, finish_two_minutes, finish_two_seconds))

	def self_connect(self, host_mx, self_port, ssl_verification, email_login, password_login):
		if self_port == 465:
			server = SMTP_SSL(host_mx, (int(self_port)), timeout=(self.timeout))
		else:
			server = SMTP(host_mx, (int(self_port)), timeout=(self.timeout))
		if ssl_verification == True:
			server.ehlo()
			server.starttls()
			server.ehlo()
		else:
			if ssl_verification == False:
				server.ehlo_or_helo_if_needed()
		server.login(email_login, password_login)
		return server

	def reset_log(self):
		try:
			os.remove(self.save_log_path)
			op = open(self.save_log_path, 'w+')
		except Exception as e:
			print(str(e))
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e

		self.show_debug_end()

	def read_log(self):
		try:
			if not os.path.isfile(self.save_log_path) or os.path.getsize(self.save_log_path) < 10:
				op = open(self.save_log_path, 'a')
				op.write('{"email_reference" : 0}')
			else:
				_JSON_DATA = loads(self.open_now(self.save_log_path, 'r'))
				if _JSON_DATA['email_reference'] > 0:
					i = input(self.cyan + '\n [X] Restore Sending Data From Email {} (y/n): '.format(_JSON_DATA['email_reference']) + self.white)
					if i in ('yes', 'y'):
						self.mailist_reference = _JSON_DATA['email_reference']
					else:
						self.mailist_reference = 0
						op = open(self.save_log_path, 'w+')
						op.write('{"email_reference" : 0}')
				else:
					print(self.green + '\n[⚠️] Starting Over ...')
		except Exception as e:
			print(str(e))
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e

	def save_log(self, em_ref):
		try:
			_JSON_DATA = loads(self.open_now(self.save_log_path, 'r'))
			_DATA_PUT = '{"email_reference" : ' + str(em_ref + 1) + '}'
			op = open(self.save_log_path, 'w+')
			op.write(_DATA_PUT)
		except Exception as e:
			print(str(e))
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e

	def countdown(self, t):
		print('\n')
		while t:
			timer = self.magenta + 'Time Sleeping is : {:02d} Seconds'.format(t)
			print(timer, end='\r')
			sleep(1)
			t -= 1

		print('\n')

	def time_calculate(self):
		time = datetime.now()
		ret = loads(self.open_now(self.timer_path, 'r'))
		start_time_one_hour = int(ret['hour'])
		start_time_one_minutes = int(ret['minute'])
		start_time_one_seconds = int(ret['second'])
		finish_time_two_hour = int(time.strftime('%H'))
		finish_two_minutes = int(time.strftime('%M'))
		finish_two_seconds = int(time.strftime('%S'))
		time_sleeping = 0
		if start_time_one_hour == finish_time_two_hour:
			if start_time_one_minutes == finish_two_minutes:
				if finish_two_seconds > start_time_one_seconds:
					time_sleeping = finish_two_seconds - start_time_one_seconds
			else:
				if finish_two_minutes > start_time_one_minutes:
					if finish_two_seconds == start_time_one_seconds:
						time_sleeping = (finish_two_minutes - start_time_one_minutes) * 60
					else:
						if finish_two_seconds > start_time_one_seconds:
							time_sleeping = (finish_two_minutes - start_time_one_minutes) * 60 + (finish_two_seconds - start_time_one_seconds)
						else:
							if finish_two_seconds < start_time_one_seconds:
								time_sleeping = (finish_two_minutes - start_time_one_minutes) * 60 + (finish_two_seconds - start_time_one_seconds)
		else:
			if finish_time_two_hour > start_time_one_hour:
				time_sleeping = (finish_time_two_hour - start_time_one_hour) * 3600
				if start_time_one_minutes == finish_two_minutes:
					if finish_two_seconds > start_time_one_seconds:
						time_sleeping += finish_two_seconds - start_time_one_seconds
				else:
					if finish_two_minutes > start_time_one_minutes:
						if finish_two_seconds == start_time_one_seconds:
							time_sleeping += (finish_two_minutes - start_time_one_minutes) * 60
						else:
							if finish_two_seconds > start_time_one_seconds:
								time_sleeping += (finish_two_minutes - start_time_one_minutes) * 60
								time_sleeping += finish_two_seconds - start_time_one_seconds
							else:
								if finish_two_seconds < start_time_one_seconds:
									time_sleeping += (finish_two_minutes - start_time_one_minutes) * 60
									time_sleeping += finish_two_seconds - start_time_one_seconds
					else:
						if finish_two_minutes < start_time_one_minutes:
							if finish_two_seconds >= start_time_one_seconds:
								time_sleeping += (finish_two_minutes - start_time_one_minutes) * 60
								time_sleeping += finish_two_seconds - start_time_one_seconds
							else:
								if finish_two_seconds < start_time_one_seconds:
									time_sleeping += (finish_two_minutes - start_time_one_minutes) * 60
									time_sleeping += finish_two_seconds - start_time_one_seconds
		if finish_two_seconds > 60 or start_time_one_seconds > 60 or start_time_one_minutes > 60 or finish_two_minutes > 60 or start_time_one_hour > 24 or finish_time_two_hour > 24:
			time_sleeping = 2000
		full_time_sleep = self.rotation['seconds_limit'] - time_sleeping
		if self.rotation['seconds_limit'] <= 0:
			self.rotation['seconds_limit'] = 1
		create_self_time = (finish_time_two_hour - start_time_one_hour) * 3600 / self.rotation['seconds_limit']
		if create_self_time < 1:
			if full_time_sleep > 0:
				self.countdown(full_time_sleep)

	def schedule_run(self):
		print('on schedl task')
		self.running(1)
		"""
		try:
			time = datetime.now()
			hours_now = int(time.strftime('%H'))
			minute_now = int(time.strftime('%M'))
			self.running(0)
			if self.schedule['activation'] == True:
				timing_start = self.schedule['timing_start']
				try:
					hours_future = int(timing_start.split(':')[0])
					minute_future = int(timing_start.split(':')[1])
					print(self.green + '\nStart Sending In : ' + self.cyan + self.schedule['timing_start'])
					while True:
						times = datetime.now()
						hours_now = int(times.strftime('%H'))
						minute_now = int(times.strftime('%M'))
						if hours_now == hours_future:
							if minute_now == minute_future:
								break
						sleep(1)

					self.running(1)
				except Exception as e:
					try:
						self.running(1)
					finally:
						e = None
						del e

			else:
				self.running(1)
		except Exception as e:
			try:
				if self.debug_read()[2]:
					print(str(e) + 'adsa')
			finally:
				e = None
				del e
		"""

	def running(self, type_data):
		try:
			json_data = loads(self.open_now(self.config_path, 'r'))
			self.subject = json_data['subject']
			self.from_name = json_data['from_name']
			self.rotation = json_data['rotation']
			self.negative_file = json_data['negative_file_path']
			self.sleep_time_between_emails = json_data['sleep_time_between_emails']
			self.attachment_file_name = json_data['attachment_file_path']
			self.email_test = json_data['email_test']
			self.sleep_after_sending_emails = json_data['sleep_after_sending_emails']
			self.unsubscribe_link = json_data['unsubscribe_link']
			self.email_bounce_validation = json_data['email_bounce_validation']
			self.link_rotation = json_data['link_rotation']
			self.base64encode = json_data['encoding_base64']
			self.reply = json_data['reply']
			self.message_id = json_data['random_message_id']
			self.return_path = json_data['return_path']
			self.auto_crypt = json_data['auto_crypt']
			self.schedule = json_data['schedule']
			self.Content_Type = json_data['Content-Type']
			self.Content_Encoding = json_data['Content-Encoding']
			self.Charset = json_data['Charset']
			self.X_Priority = json_data['X-Priority']
			self.translate = json_data['translate']
			self.vpn_data = json_data['vpn_auto_change']
			self.remove_dupl = json_data['remove_mailists_dpl']
			self.bcc = json_data['bcc']
			if type_data == 1:
				self.auto_email_send()
		except Exception as e:
			print(str(e))
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e


class banner_run:

	def run_banner(self):
		try:
			clear = '\x1b[0m'
			colors = [36,32,34,35,31,37]
			x = get(Anonym_Sender().alpha_logo).text
			for N, line in enumerate(x.split('\n')):
				sys.stdout.write('\x1b[1;%dm%s%s\n' % (choice(colors), line, clear))
				sleep(0.03)

		except Exception as e:
			print(str(e))
			try:
				if self.debug_read()[2]:
					print(str(e))
			finally:
				e = None
				del e


class random_o:

	def __init__(self):
		self.random_country = loads(Anonym_Sender().open_now(Anonym_Sender().country_path, 'r'))
		self.random_os = loads(Anonym_Sender().open_now(Anonym_Sender().os_path, 'r'))
		self.random_browser = loads(Anonym_Sender().open_now(Anonym_Sender().browser_path, 'r'))


class cls_print:

	def auto_print(self, int_, mailist_reference, email, host):
		Anonym_Sender().save_log(mailist_reference)
		mailist_reference += 1
		if int_ == 1:
			print(Anonym_Sender().cyan + '[{}]'.format(str(mailist_reference)) + Anonym_Sender().green + '[SUCCESS] ++ ' + Anonym_Sender().yellow + 'FROM ' + Anonym_Sender().white + host + Anonym_Sender().yellow + ' TO ' + Anonym_Sender().white + email + Anonym_Sender().reset)
		else:
			if int_ == 2:
				print(Anonym_Sender().cyan + '[{}]'.format(str(mailist_reference + 1)) + Anonym_Sender().red + '[FAILED] ' + Anonym_Sender().yellow + ' => ' + Anonym_Sender().white + email + Anonym_Sender().reset)
			else:
				if int_ == 3:
					print(Anonym_Sender().cyan + '[{}]'.format(str(mailist_reference)) + Anonym_Sender().green + '[SUCCESS] ++ ' + Anonym_Sender().yellow + 'FROM ' + Anonym_Sender().white + host + Anonym_Sender().yellow + ' TO ' + Anonym_Sender().white + email + Anonym_Sender().green + '    [VALID]' + Anonym_Sender().reset)
				else:
					if int_ == 4:
						print(Anonym_Sender().cyan + '[{}]'.format(str(mailist_reference)) + Anonym_Sender().red + '[FAILED] ' + Anonym_Sender().yellow + ' => ' + Anonym_Sender().white + email + Anonym_Sender().red + '    [INVALID]' + Anonym_Sender().reset)
					else:
						if int_ == 5:
							print(Anonym_Sender().cyan + '[{}]'.format(str(mailist_reference)) + Anonym_Sender().green + '[SUCCESS] ++ ' + Anonym_Sender().yellow + 'FROM ' + Anonym_Sender().white + host + Anonym_Sender().yellow + ' TO ' + Anonym_Sender().white + Anonym_Sender().red + '    [BLACKLISTED]' + Anonym_Sender().reset)


class debouncer:

	def __init__(self):
		self.timeout = 15
		self.path_dir = 'data_emails'
		self.name_text = ['valid_data.txt', 'invalid_data.txt', 'blacklisted.txt']

	def read_file(self, filename):
		try:
			op = open(filename)
			return op.read()
		except Exception as e:
			print(str(e))
			try:
				print(str(e))
			finally:
				e = None
				del e

	def create_file(self):
		try:
			for files in self.name_text:
				if not os.path.exists(self.path_dir + '/' + files):
					op = open(self.path_dir + '/' + files, 'a')

		except:
			pass

	def data_email_save(self, email, _debouncer__type):
		try:
			if os.path.isdir(self.path_dir):
				try:
					self.create_file()
					if _debouncer__type == 1:
						if email not in self.read_file('./' + self.path_dir + '/' + self.name_text[0]):
							file_put = open('./' + self.path_dir + '/' + self.name_text[0], 'a')
							file_put.write(email + '\n')
					else:
						if _debouncer__type == 2:
							if email not in self.read_file('./' + self.path_dir + '/' + self.name_text[1]):
								file_put = open('./' + self.path_dir + '/' + self.name_text[1], 'a')
								file_put.write(email + '\n')
						else:
							if _debouncer__type == 3:
								if email not in self.read_file('./' + self.path_dir + '/' + self.name_text[2]):
									file_put = open('./' + self.path_dir + '/' + self.name_text[2], 'a')
									file_put.write(email + '\n')
				except Exception as e:
					print(str(e))
					try:
						print(str(e))
					finally:
						e = None
						del e

			else:
				os.mkdir(self.path_dir)
				self.data_email_save(email, _debouncer__type)
		except Exception as e:
			try:
				print(str(e))
			finally:
				e = None
				del e

	def dns_resolver(self, domain):
		try:
			if 'yahoo.fr' in domain:
				return 'mx-eu.mail.am0.yahoodns.net'
			if 'yahoo.com' in domain:
				return 'mta5.am0.yahoodns.net'
			records = dns.resolver.resolve(domain, 'MX')
			mxRecord = records[0].exchange
			mxRecord = str(mxRecord)
			return mxRecord
		except:
			return domain

	def verify(self, from_email, email, debug_level):
		try:
			host = gethostname()
			domain = email.split('@')[1]
			server = SMTP()
			server.set_debuglevel(debug_level)
			server.timeout = self.timeout
			server.connect(self.dns_resolver(domain))
			server.helo(host)
			server.mail('<' + from_email + '>')
			code, message = server.rcpt(str(email))
			if code == 250:
				self.data_email_save(email, 1)
				return 3
			if code == 503:
				self.data_email_save(email, 3)
				return 5
			self.data_email_save(email, 2)
			return 4
		except:
			self.data_email_save(email, 2)
			return 4


class smtplib_exceptions:

	def self_extract_code(self, text):
		try:
			i = 0
			while i < len(text):
				if text[i].isdigit():
					if text[i + 1].isdigit():
						if text[i + 2].isdigit():
							if not text[i + 3].isdigit():
								return text[i] + text[i + 1] + text[i + 2]
							i += 1

		except:
			pass

	def raise_verify(self, text):
		try:
			if text in ('Connection unexpectedly closed', 'Connection unexpectedly closed: The read operation timed out',
						'SMTP AUTH extension not supported by server.', 'please run connect() first',
						'Connection unexpectedly closed: timed out'):
				return 10061
			if 'The mail server could not deliver mail' in text:
				return 501
			if 'SMTP AUTH extension not supported by server.' in text:
				return 104
			if 'timed out' in text:
				return 535
			if 'may not exist' in text:
				return 234
			if 'Errno 11001' in text:
				return 11001
			if 'An established connection was aborted by the software in your host machine' in text or 'A socket operation was attempted' in text:
				return 10054
			if 'A connection attempt failed because' in text or 'Une tentative de connexion a échoué' in text or 'Aucune connexion n’a pu être' in text or 'No connection could be made because the target machine actively refused it' in text or 'getaddrinfo failed' in text or 'Connection timed out' in text:
				return 10061
			if text in ('[Errno -2] Name or service not known', ):
				return -2
			if 'Reject for policy reason' in text:
				return 571
			if 'too much mail from' in text:
				return 999
			code_smtp_exception = self.self_extract_code(text)
			return int(code_smtp_exception)
		except:
			pass


class management_newsletters:

	def unsubscribe_add(self, user, email_to, body_type):
		text_html = '<p style="color: rgb(136, 136, 136); font-family: sans-serif; font-size: 12px; text-align: center; background-color: rgb(251, 252, 252);text-align: center;">If you no longer wish to receive these emails, you can <a href="##link_unsubscribe##" rel="noopener" style="color: rgb(75, 108, 183); text-decoration-line: none;" target="_blank">unsubscribe</a>.</p>'
		text_plain = '\n\nIf you no longer wish to receive these emails, you can unsubscribe -> ##link_unsubscribe##'
		if body_type == 0:
			data_increase = text_plain.replace('##link_unsubscribe##', self.unsubscribe_link_generator(user, email_to))
			return data_increase
		data_increase = text_html.replace('##link_unsubscribe##', self.unsubscribe_link_generator(user, email_to))
		return data_increase

	def unsubscribe_link_generator(self, user, email_to):
		link = 'https://{}/unsubscribe.php?email={}'.format(user, email_to)
		return link


class crypto:

	def __init__(self):
		self.data_rep = {
		  'А': 'A', 'В': 'B', 'Е': 'E', 'М': 'M', 'Н': 'H', 'О': 'O', 'а': 'a', 'е': 'e', 'о': 'o', 'Р': 'P', 'с': 'c', 'у': 'y', 'Х': 'X', 'Т': 'T', 'і': 'i', 'ѵ': 'v'}

	def replace_all(self, text, dic):
		for i, j in dic.items():
			text = text.replace(i, j)

		return text

	def unescape(self, raw_text):
		html_decoded_string = unescape(raw_text)
		return html_decoded_string

	def start_crypt(self):
		try:
			op = open((Anonym_Sender().letter), encoding='utf-8')
			set_up = op.read().replace('\t', '').replace('\n', '')
			set_up = self.unescape(set_up)
			if '<p>' or 'div' or 'table' or '<a' or 'href' in set_up:
				val = findall('>(.*?)<', set_up)
				full_strings = []
				for values in val:
					values = values.strip()
					if values:
						if '##email_user##' not in values:
							if '##email##' not in values:
								full_strings.append(values)

				strings_replaced = []
				for strings in full_strings:
					for i, j in self.data_rep.items():
						strings = strings.replace(j, i)

					strings_replaced.append(strings)

				strings_manager = {}
				i = 0
				for key_b in full_strings:
					strings_manager[key_b] = strings_replaced[i]
					i += 1

				new_letter = self.replace_all(set_up, strings_manager)
				if 'utf-8' not in new_letter:
					new_letter = '<meta charset="utf-8">' + new_letter
				self.letter = new_letter
			else:
				self.letter = set_up
		except Exception as e:
			try:
				print(str(e))
			finally:
				e = None
				del e


class mix_random:

	def random_data(self, length, type_r):
		if type_r == 'digits':
			letters = digits
			return ''.join((choice(letters) for i in range(length)))
		if type_r == 'alpha':
			letters = ascii_uppercase + ascii_lowercase
			return ''.join((choice(letters) for i in range(length)))
		if type_r == 'hex':
			letters = hexdigits
			return ''.join((choice(letters) for i in range(length)))


class email_regex:

	def email_valid(self, email):
		try:
			regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\\.[A-Z|a-z]{2,})+'
			if search(regex, email):
				return 1
			return 0
		except Exception as e:
			try:
				return 0
			finally:
				e = None
				del e


class run_pmta:

	def class_make(self):
		try:
			os.system('cls')
			banner_run().run_banner()
			try:
				x = str(input(Anonym_Sender().yellow + '\n⚜️ Wanna Start Sending yes/no : ' + Anonym_Sender().reset))
			except:
				print(Anonym_Sender().bright + '\n\n ;)  Ok Next Time Sir')
				#sys.exit()

			x = x.lower()
			if len(x) > 0 and x.lower()[0] == 'y':
				print(Anonym_Sender().green + '\n ✅ Start Sending Now ...\n')
				#Anonym_Sender().schedule_run()
				Anonym_Sender().running(1)
			else:
				print(Anonym_Sender().bright + '\n 👌 Ok Next Time Sir')
				#sys.exit()
		except:
			pass

	def read_activation(self):
		try:
			#res = post((Anonym_Sender().api_manage.strip()), headers=(Anonym_Sender().headers), data={'mac': Anonym_Sender().get_mac()})
			#return int(res.text)
			return 1
		except Exception as e:
			try:
				return 0
			finally:
				e = None
				del e

	def pmta_run(self):
		try:
			os.system('cls')
			banner_run().run_banner()
			mac_address = Anonym_Sender().get_mac()
			if self.read_activation() == 1:
				print(Anonym_Sender().green + '\n\n [LOGGING SUCCESS FROM] -> ' + Anonym_Sender().white + mac_address)
				sleep(1)
				self.class_make()
			else:
				print(Anonym_Sender().red + '\n ❌ Invalid Machine :(\n\n {}Contact -> {}@brendonurie2000'.format(Anonym_Sender().reset, Anonym_Sender().green))
				print(Anonym_Sender().green + '\n Your Machine Address : ' + Anonym_Sender().white + mac_address)
				#sys.exit()
		except KeyboardInterrupt:
			print(Anonym_Sender().red + '\n Something Wrong :( ->\n Contact {}@brendonurie2000'.format(Anonym_Sender().green))
			#sys.exit()


run_pmta().pmta_run()