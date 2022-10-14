import xml.etree.ElementTree as Xet
import sys
import csv

def scrape():
	tree = Xet.parse(sys.argv[1])
	analysis = tree.getroot().find('analysis')

	total_number_of_event_terms = 0
	total_number_of_discourse_terms = 0
	total_number_of_pd_terms = 0
	total_number_of_topos_terms = 0

	event_count_tracker = dict()
	discourse_count_tracker = dict()
	pd_count_tracker = dict()
	topos_count_tracker = dict()

	paragraph_tracker = dict()

	category_tracker = dict()

	# tracker_pairs = [[event_count_tracker, "event", total_number_of_event_terms], [discourse_count_tracker, "discourse", total_number_of_discourse_terms], [pd_count_tracker, "personaDescription", total_number_of_pd_terms], [topos_count_tracker, "topos", total_number_of_topos_terms]]

	# for tracker_pair in tracker_pairs:
	# 	for item in analysis.findall(tracker_pair[1]):
	# 		if item[0].tag == "textUnitReference":
	# 			paragraph_number = item.find('textUnitReference').text
	# 			if paragraph_number not in paragraph_tracker:
	# 				paragraph_tracker[paragraph_number] = ""

	# 			for term in item.findall('type'):
	# 				tracker_pair[2] += 1
	# 				paragraph_tracker[paragraph_number] += term.text.strip() + "&&&"
	# 				if term.text.strip() in tracker_pair[0]:
	# 					tracker_pair[0][term.text.strip()] += 1
	# 				else:
	# 					tracker_pair[0][term.text.strip()] = 1
	# 		else:
	# 			start_paragraph = item.find("textUnitRangeReference").find("start").text
	# 			end_paragraph = item.find("textUnitRangeReference").find("end").text
	# 			for x in range(int(start_paragraph), int(end_paragraph)+1):
	# 				if x not in paragraph_tracker:
	# 					paragraph_tracker[x] = ""

	# 				for term in item.findall('type'):
	# 					paragraph_tracker[x] += term.text.strip() + "&&&"
	# 					tracker_pair[2] += 1
	# 					if term.text.strip() in tracker_pair[0]:
	# 						tracker_pair[0][term.text.strip()] += 1
	# 					else:
	# 						tracker_pair[0][term.text.strip()] = 1

	#could combine the four w the list [event, discourse, pd, topos]

	for event in analysis.findall('event'):
		if event[0].tag == "textUnitReference":
			paragraph_number = event.find('textUnitReference').text
			if paragraph_number not in paragraph_tracker:
				paragraph_tracker[paragraph_number] = ""

			for term in event.findall('type'):
				term_name = term.text.strip().strip()
				if (term_name == "grieving"):
					term_name = "grieving (event)"
				if (term_name == "conversion"):
					term_name = "conversion (event)"
				total_number_of_event_terms += 1
				paragraph_tracker[paragraph_number] += term_name + "&&&"
				if term_name in event_count_tracker:
					event_count_tracker[term_name] += 1
				else:
					event_count_tracker[term_name] = 1
					category_tracker[term_name] = "EVENT"
		else:
			start_paragraph = event.find("textUnitRangeReference").find("start").text
			end_paragraph = event.find("textUnitRangeReference").find("end").text
			for x in range(int(start_paragraph), int(end_paragraph)+1):
				if x not in paragraph_tracker:
					paragraph_tracker[x] = ""

				for term in event.findall('type'):
					term_name = term.text.strip()
					if (term_name == "grieving"):
						term_name = "grieving (event)"
					if (term_name == "conversion"):
						term_name = "conversion (event)"
					paragraph_tracker[x] += term_name + "&&&"
					total_number_of_event_terms += 1
					if term_name in event_count_tracker:
						event_count_tracker[term_name] += 1
					else:
						event_count_tracker[term_name] = 1
						category_tracker[term_name] = "EVENT"

	for discourse in analysis.findall('discourse'):
		if discourse[0].tag == "textUnitReference":
			paragraph_number = discourse.find('textUnitReference').text
			if paragraph_number not in paragraph_tracker:
				paragraph_tracker[paragraph_number] = ""

			for term in discourse.findall('type'):
				paragraph_tracker[paragraph_number] += term.text.strip() + "&&&"
				total_number_of_discourse_terms += 1
				if term.text.strip() in discourse_count_tracker:
					discourse_count_tracker[term.text.strip()] += 1
				else:
					discourse_count_tracker[term.text.strip()] = 1
					category_tracker[term.text.strip()] = "DISCOURSE"
		else:
			start_paragraph = discourse.find("textUnitRangeReference").find("start").text
			end_paragraph = discourse.find("textUnitRangeReference").find("end").text
			for x in range(int(start_paragraph), int(end_paragraph)+1):
				if x not in paragraph_tracker:
					paragraph_tracker[x] = ""

				for term in discourse.findall('type'):
					paragraph_tracker[x] += term.text.strip() + "&&&"
					total_number_of_discourse_terms += 1
					if term.text.strip() in discourse_count_tracker:
						discourse_count_tracker[term.text.strip()] += 1
					else:
						discourse_count_tracker[term.text.strip()] = 1
						category_tracker[term.text.strip()] = "DISCOURSE"

	for pd in analysis.findall('personaDescription'):
		if pd[0].tag == "textUnitReference":
			paragraph_number = pd.find('textUnitReference').text
			if paragraph_number not in paragraph_tracker:
				paragraph_tracker[paragraph_number] = ""

			for term in pd.findall('type'):
				term_name = term.text.strip()
				if (term_name == "grieving"):
					term_name = "grieving (PD)"
				paragraph_tracker[paragraph_number] += term_name + "&&&"
				total_number_of_pd_terms += 1
				if term_name in pd_count_tracker:
					pd_count_tracker[term_name] += 1
				else:
					pd_count_tracker[term_name] = 1
					category_tracker[term_name] = "PD"
		else:
			start_paragraph = pd.find("textUnitRangeReference").find("start").text
			end_paragraph = pd.find("textUnitRangeReference").find("end").text
			for x in range(int(start_paragraph), int(end_paragraph)+1):
				if x not in paragraph_tracker:
					paragraph_tracker[x] = ""

				for term in pd.findall('type'):
					term_name = term.text.strip()
					if (term_name == "grieving"):
						term_name = "grieving (PD)"
					paragraph_tracker[x] += term_name + "&&&"
					total_number_of_pd_terms += 1
					if term.text.strip() in pd_count_tracker:
						pd_count_tracker[term_name] += 1
					else:
						pd_count_tracker[term_name] = 1
						category_tracker[term_name] = "PD"

	for topos in analysis.findall('topos'):
		if topos[0].tag == "textUnitReference":
			paragraph_number = topos.find('textUnitReference').text
			if paragraph_number not in paragraph_tracker:
				paragraph_tracker[paragraph_number] = ""

			for term in topos.findall('type'):
				term_name = term.text.strip()
				if (term_name == "conversion"):
					term_name = "conversion (topos)"
				paragraph_tracker[paragraph_number] += term_name + "&&&"
				total_number_of_topos_terms += 1
				if term_name in topos_count_tracker:
					topos_count_tracker[term_name] += 1
				else:
					topos_count_tracker[term_name] = 1
					category_tracker[term_name] = "TOPOS"
		else:
			start_paragraph = topos.find("textUnitRangeReference").find("start").text
			end_paragraph = topos.find("textUnitRangeReference").find("end").text
			for x in range(int(start_paragraph), int(end_paragraph)+1):
				if x not in paragraph_tracker:
					paragraph_tracker[x] = ""

				for term in topos.findall('type'):
					term_name = term.text.strip()
					if (term_name == "conversion"):
						term_name = "conversion (topos)"
					paragraph_tracker[x] += term_name + "&&&"
					total_number_of_topos_terms += 1
					if term_name in topos_count_tracker:
						topos_count_tracker[term_name] += 1
					else:
						topos_count_tracker[term_name] = 1
						category_tracker[term_name] = "TOPOS"

	term_concurrence_tracker = dict()
	cross_category_concurrence_tracker = dict()

	for key in paragraph_tracker:
		values_in_paragraph = paragraph_tracker[key].split("&&&")[:-1]
		already_counted = dict()
		for x in range(len(values_in_paragraph)):
			for y in range(x+1, len(values_in_paragraph)):
				value_set = frozenset((values_in_paragraph[x], values_in_paragraph[y]))
				if ((value_set not in already_counted) or (not already_counted[value_set])):
					if (value_set in term_concurrence_tracker):
						term_concurrence_tracker[value_set] +=1
					else:
						term_concurrence_tracker[value_set] = 1

					if (category_tracker[values_in_paragraph[x]] != category_tracker[values_in_paragraph[y]]):
						if (value_set in cross_category_concurrence_tracker):
							cross_category_concurrence_tracker[value_set] +=1
						else:
							cross_category_concurrence_tracker[value_set] = 1
					already_counted[value_set] = True

	with open('term_concurrence_counter.txt', 'w') as f:
		f.write("first term:::second term:::# of concurrences:::first term's total count:::second term's total count:::first term concurrence rate:::second term concurrence rate\n")
		for key in term_concurrence_tracker.keys():
			first_term = tuple(key)[0]
			if len(tuple(key)) == 1:
				second_term = tuple(key)[0]
			else:
				second_term = tuple(key)[1]

			trackers = [event_count_tracker,discourse_count_tracker,pd_count_tracker,topos_count_tracker]

			for tracker in trackers:
				if first_term in tracker:
					first_term_count = tracker[first_term]
				if second_term in tracker:
					second_term_count = tracker[second_term]

			first_term_rate = term_concurrence_tracker[key]/first_term_count
			second_term_rate = term_concurrence_tracker[key]/second_term_count

			f.write("%s:::%s:::%s:::%s:::%s:::%s:::%s\n"%(first_term,second_term,term_concurrence_tracker[key],first_term_count,second_term_count, first_term_rate, second_term_rate))

	with open('cross_category_concurrence_counter.txt', 'w') as f:
		f.write("first term:::second term:::# of concurrences:::first term's total count:::second term's total count:::first term concurrence rate:::second term concurrence rate\n")
		for key in cross_category_concurrence_tracker.keys():
			first_term = tuple(key)[0]
			second_term = tuple(key)[1]

			trackers = [event_count_tracker,discourse_count_tracker,pd_count_tracker,topos_count_tracker]

			for tracker in trackers:
				if first_term in tracker:
					first_term_count = tracker[first_term]
				if second_term in tracker:
					second_term_count = tracker[second_term]

			first_term_rate = cross_category_concurrence_tracker[key]/first_term_count
			second_term_rate = cross_category_concurrence_tracker[key]/second_term_count

			f.write("%s:::%s:::%s:::%s:::%s:::%s:::%s\n"%(first_term,second_term,cross_category_concurrence_tracker[key],first_term_count,second_term_count, first_term_rate, second_term_rate))

	with open('total_counter.txt', 'w') as f:
		f.write("Event count: " + str(total_number_of_event_terms) + "\n")
		f.write("Discourse count: " + str(total_number_of_discourse_terms) + "\n")
		f.write("Persona description count: " + str(total_number_of_pd_terms) + "\n")
		f.write("Topos count: " + str(total_number_of_topos_terms) + "\n")

	with open('term_counter.txt', 'w') as f:
		for key in event_count_tracker.keys():
			f.write("%s:::%s\n"%(key,event_count_tracker[key]))
		for key in discourse_count_tracker.keys():
			f.write("%s:::%s\n"%(key,discourse_count_tracker[key]))
		for key in pd_count_tracker.keys():
			f.write("%s:::%s\n"%(key,pd_count_tracker[key]))
		for key in topos_count_tracker.keys():
			f.write("%s:::%s\n"%(key,topos_count_tracker[key]))

if __name__ == '__main__':
	scrape()
	#pass the BESS file as the first argument