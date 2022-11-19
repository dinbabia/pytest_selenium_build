# import fitz  #pip install PyMuPDF

# class PDFActions:

#     def Close_PDF(self, pdf_doc):
#         '''Close the pdf file
#         --------------------------------
#         * @param: pdf_file -> The returned object from function "init_pdf"
#         '''
#         pdf_doc.close()

#     def get_all_hyperlinks_from_pdf(self, pdf_doc, part_numbers):
#         '''Get all the hyperlinks from pdf. 0 = uri.
#         ----------------------------
#         * @param: pdf_file -> The returned object from function "init_pdf"
#         * @param: web_part_numbers -> The part numbers fetched from the website. Stored in the dictionary {data["part-numbers"]} from the test case.
#         * @return: test_data -> A dictionary that consist of shareable link and all part numbers links.
#         '''
#         test_data = {
#         "shareable-link" : "",
#         "parts_links" : []
#         }

#         count =0
#         for page in pdf_doc:
#                 if count == 0:
#                     test_data['shareable-link'] = page.get_links()[0]['uri']

#                     for x in range (4, len(part_numbers) + 4):
#                         test_data['parts_links'].append(page.get_links()[x]['uri'])
#                 count += 1
#         return test_data

#     def get_all_words_from_pdf_specific_page(self, pdf_doc, page_number):
#         '''Get all words from the pdf in a specific page number
#         --------------------------------
#         * @param: pdf_doc -> The returned object from function "init_pdf"
#         * @param: page_number -> The page number of the pdf file.
#         * @return: page_one_words -> A list of all strings/words from the specifid page of pdf.
#         '''
#         try:
#             with fitz.open(pdf_doc) as doc:

#                 collate_text = []
#                 page_one_words = []
                
#                 for page in doc:
#                     collate_text.append(page.get_text())
                
#                 min = 0
#                 max = len(collate_text[page_number -1])
#                 while min < max:
#                     index = collate_text[page_number -1][min:max].find('\n') + min
#                     new_word = collate_text[page_number -1][min:index]
#                     page_one_words.append(new_word)
#                     min = index + 1
#         except:
#             print("No specific page found.")
#         return page_one_words

#     def get_part_numbers_index(self, page_one_words_actions, part_numbers):
#         '''Get all the hyperlinks from pdf. 0 = uri.
#         ----------------------------
#         * @param: page_one_words_actions -> All words fetched from function [get_all_words_from_pdf_specific_page]
#         * @param: part_numbers -> The part numbers fetched from the website. Stored in the dictionary {data["part-numbers"]} from the test case.
#         * @return: sort_index -> A list of all index of the sorted values
#         '''
#         indexes = []
#         for x in range(0,len(part_numbers)):
#             add = page_one_words_actions.index(part_numbers[x])
#             indexes.append(add)
            
#         return indexes

#     def get_search_param_index(self, page_one_words_actions, search_params):
#         '''Get all the hyperlinks from pdf. 0 = uri.
#         ----------------------------
#         * @param: page_one_words_actions -> All words fetched from function [get_all_words_from_pdf_specific_page]
#         * @param: search_params -> The search parameters fetched from the website. Stored in the dictionary {data["search_param_values"]} from the test case.
#         * @return: sort_index -> A list of all index of the sorted values
#         '''
#         indexes = {
#             'search_type_index' : 0,
#             'last_index' : 0
#         }
#         web_last_index = len(search_params) - 1
#         for x in range(0,len(page_one_words_actions)):
#             if page_one_words_actions[x] == search_params[0]:
#                 indexes['search_type_index'] = x
#             elif page_one_words_actions[x] == search_params[web_last_index]:
#                 indexes['last_index'] = x

#         return indexes

#     def get_sort_values_index(self, page_one_words_actions, part_numbers):
#         '''Get all the hyperlinks from pdf. 0 = uri.
#         ----------------------------
#         * @param: page_one_words_actions -> All words fetched from function [get_all_words_from_pdf_specific_page]
#         * @param: part_numbers -> The part numbers fetched from the website. Stored in the dictionary {data["part-numbers"]} from the test case.
#         * @return: sort_index -> A list of all index of the sorted values
#         '''
#         sort_index = []
#         for part in range(0, len(part_numbers)):
#             add =  page_one_words_actions.index(part_numbers[part]) + 1
#             sort_index.append(add)
#         return sort_index
    
#     def get_all_result_images(self, pdf_file, number_of_pages=1):
#         '''Get all the hyperlinks from pdf. 0 = uri.
#         ----------------------------
#         * @param: pdf_file -> All words fetched from function [get_all_words_from_pdf_specific_page]
#         * @param: number_of_pages -> The part numbers fetched from the website. Stored in the dictionary {data["part-numbers"]} from the test case.
#         * @return: images -> A list of all FlateDecoded images 
#         '''
#         images = []
#         doc = self.Read_Pdf(pdf_file)
#         for page in range(1, number_of_pages):
#             for img in doc.get_page_images(page):
#                 images.append(img)
#         return images

#     def parts_link_from_pdf(self, pdf_doc, web_part_numbers):
#         '''Return the part numbers link from [get_all_hyperlinks_from_pdf]
#         --------------------------------
#         * @param: pdf_doc -> The returned object from function "init_pdf"
#         * @param: web_part_numbers -> The part numbers fetched from the website. Stored in the dictionary {data["part-numbers"]} from the test case.
#         * @return: links['parts_links'] -> A list of all part numbers links
#         '''
#         links = self.get_all_hyperlinks_from_pdf(pdf_doc, web_part_numbers)
#         return links['parts_links']

#     def Read_Pdf(self, filename):
#         '''Start/Open the pdf file
#         --------------------------------
#         * @param: filename -> The relative from src address of the downloaded pdf file.
#         * @return: pdf_file -> The opened/read file from PyMuPDF action
#         '''
#         doc = fitz.open(filename)
#         return doc

#     def shareable_link_from_pdf(self, pdf_doc, web_part_numbers):
#         '''Return the shareable link from [get_all_hyperlinks_from_pdf]
#         --------------------------------
#         * @param: pdf_doc -> The returned object from function "init_pdf"
#         * @param: web_part_numbers -> The part numbers fetched from the website. Stored in the dictionary {data["part-numbers"]} from the test case.
#         * @return: links['shareable-link'] -> The shareable link from the pdf
#         '''
#         links = self.get_all_hyperlinks_from_pdf(pdf_doc, web_part_numbers)
#         return links['shareable-link']

#     def table_column_names_start_index(self, page_one_words_actions):
#         '''Get the start and end index of the table headers which are the column names.
#         --------------------------------
#         * @param: page_one_words_actions -> All words fetched from function [get_all_words_from_pdf_specific_page]
#         * @return: indexes -> The part number (starting) and price (end) index dictionary
#         '''
#         indexes = {
#             'part_number_index' : 0,
#             'price_index' : 0
#         }
#         for x in range(0,len(page_one_words_actions)):
        
#             if page_one_words_actions[x].lower() == 'part number':
#                 indexes['part_number_index'] = x
#             elif page_one_words_actions[x].lower() == 'price':
#                 indexes['price_index'] = x
#             x += 1
        
#         return indexes

    

    
    


    

                

