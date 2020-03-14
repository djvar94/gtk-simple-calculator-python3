#!/usr/bin/env python3
import sys
import gi
import operator
from gi.repository import Gtk
gi.require_version("Gtk", "3.0")


class Handlers:

    def on_main_Window_destroy(self, *args, data=None):
        Gtk.main_quit()

    def on_clearButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.set_buffer()
        expressionField = buffer

    def on_zeroButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("0")
        expressionField = finalText

    def on_oneButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("1")
        expressionField = finalText

    def on_twoButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("2")
        expressionField = finalText

    def on_threeButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("3")
        expressionField = finalText

    def on_fourButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("4")
        expressionField = finalText

    def on_fiveButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("5")
        expressionField = finalText

    def on_sixButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("6")
        expressionField = finalText

    def on_sevenButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("7")
        expressionField = finalText

    def on_eightButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("8")
        expressionField = finalText

    def on_nineButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("9")
        expressionField = finalText

    def on_plusButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("+")
        expressionField = finalText

    def on_minusButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("-")
        expressionField = finalText

    def on_multiplyButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("x")
        expressionField = finalText

    def on_divideButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("÷")
        expressionField = finalText

    def on_percentageButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("%")
        expressionField = finalText

    def on_dotButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor(".")
        expressionField = finalText

    def on_openParenthesisButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor("(")
        expressionField = finalText

    def on_closeParenthesisButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.insert_at_cursor(")")
        expressionField = finalText

    def on_backButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        end = buffer.get_end_iter()
        finalText = buffer.backspace(end, False, True)
        expressionField = finalText

    def on_equalsButton_clicked(self, button, data=None):
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        start = buffer.get_start_iter()
        end = buffer.get_end_iter()
        expression = buffer.get_text(start, end, False)

        if expression is not (""):
            try:
                expression = expression.replace('x', '*')
                expression = expression.replace('÷', '/')
                expression = expression.replace('%', '/100')
                calculation = str(eval(expression))
                result = buffer.insert_at_cursor("=" + "\n" + calculation)

            except (SyntaxError, NameError):
                invalid_Expression_Dialog = builder.get_object(
                    "invalid_Expression_Dialog")
                invalid_Expression_Dialog.show()

        else:
            pass

    def on_invalidExpressionButton_clicked(self, button, data=None):
        invalid_Expression_Dialog = builder.get_object(
            "invalid_Expression_Dialog")
        invalid_Expression_Dialog.hide()
        expressionField = builder.get_object("expressionField")
        buffer = expressionField.get_buffer()
        finalText = buffer.set_text("")
        expressionField = finalText


builder = Gtk.Builder()
builder.add_from_file("Simple Calculator UI.glade")
builder.connect_signals(Handlers())

main_Window = builder.get_object("main_Window")
main_Window.show()

Gtk.main()
