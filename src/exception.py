import sys
import logging

def error_message_detail(error, error_detail:sys):
    _, _, tb = error_detail.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    error_message = "Error occured in file:[{0}] at line number:[{1}] with error message:[{2}]".format(file_name, tb.tb_lineno, error)
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error = error
        self.error_detail = error_detail
        self.error_message = error_message_detail(self.error, self.error_detail)
        

    def __str__(self):
        return self.error_message
    

