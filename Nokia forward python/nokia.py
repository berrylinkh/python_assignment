nokia_menu = """

        Application

        1  PhoneBook
        2  Message
        3  Chat
        4  Call register
        5  Tones
        6  Settings
        7  Call Divert
        8  Games
        9  Calculator
        10 Reminder
        11 Clock
        12 Profiles
        13 Sim Service

        Select option:
"""

main_menu_list = int(input(nokia_menu))
match main_menu_list:

    case 1:
        print("PhoneBook")
        phonebook_menu = """
                1  Search
                2  Service number
                3  Add name
                4  Erase
                5  Edit
                6  Assign tones
                7  Send b'card
                8  Option
                9  Speed dial
                10 Voice tags
                0 Back

                Select option:
        """
        phonebook_menu_list = int(input(phonebook_menu))
        match phonebook_menu_list:

            case 1:
                print("Search")
            case 2:
                print("Service number")
            case 3:
                print("Add name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Assign tones")
            case 7:
                print("Send b'card")
            case 8:
                print("Option")
                option_menu = """

                        1 Type of view
                        2 Memory status
                        0 Back to phonebook

                        Select option:
                """
                option_menu_list = int(input(option_menu))
                match option_menu_list:

                    case 1:
                        print("Type of view")
                    case 2:
                        print("Memory status")
                    case 0:
                        print("Back to phonebook")

            case 9:
                print("Speed dial")
            case 10:
                print("Voice tags")
            case 0:
                print("Exit")

    case 2:
        print("Message")
        message_menu = """

        1  Write message
        2  Inbox
        3  Outbox
        4  Picture
        5  Templates
        6  Smileys
        7  Message settings
        8  Info service
        9  Voice mailbox number
        10 Service command editor
        0  Back to Nokia menu

        Select option:
        """
        message_menu_list = int(input(message_menu))
        match message_menu_list:
            case 1:
                print(" Write message")
            case 2:
                print("Inbox")
            case 3:
                print(" Outbox")
            case 4:
                print(" Picture")
            case 5:
                print("Templates")
            case 6:
                print("Smileys")
            case 7:
                print("Message settings")
                message_settings_menu = """
                1 Set 1
                2 Common
                0 Back to message Menu

                Select option:
                """
                message_settings_menu_list = int(input(message_settings_menu))
                match message_settings_menu_list:
                    case 1:
                        print("set 1")
                        set1_menu = """

                        1  Message centre number
                        2  Message sent as
                        3  Message validity
                        0  Back to message settings

                        Select option:
                        """

                        set1_menu_list = int(input(set1_menu))
                        match set1_menu_list:
                            case 1:
                                print("Message centre number")
                            case 2:
                                print("Message sent as")
                            case 3:
                                print(" Message validity")
                            case 0:
                                print("Back to message settings")

                    case 2:
                        print("common")
                        common_menu = """

                        1 Delivery report
                        2 Reply via same centre
                        3 Character support
                        0 Back to message settings

                        Select option:
                        """

                        common_menu_list = int(input(common_menu))
                        match common_menu_list:
                            case 1:
                                print("Delivery report")
                            case 2:
                                print("Reply via same centre")
                            case 3:
                                print(" Character support")
                            case 0:
                                print("Back to message settings")

                    case 0:
                        print("Back to message Menu")

            case 8:
                print("Info service")
            case 9:
                print("Voice mailbox number")
            case 10:
                print("Service command editor")
            case 0:
                print("Exit")

    case 3:
        print("Chat")

    case 4:
        print("Call register")
        call_register_menu = """

        1  Missed calls
        2  Recieved calls
        3  Dialed number
        4  Erase recent call list
        5  Show all call duration
        6  Show call cost
        7  Call cost settings
        8  Perpaid credit
        0 Back to Nokia menu

        Select option:
        """

        call_register_menu_list = int(input(call_register_menu))
        match call_register_menu_list:
            case 1:
                print("Missed calls")
            case 2:
                print("Recieved calls")
            case 3:
                print("Dialed number")
            case 4:
                print("Erase recent call list")
            case 5:
                print("Show all call Duration")
                show_all_call_duration_menu = """

                1  Last call duration
                2  All call duration
                3  Recieved call duration
                4  Dailed call duration
                5  Clear timer
                0 Back to call register

                Select option:
                """
                show_all_call_duration_menu_list = int(input(show_all_call_duration_menu))
                match show_all_call_duration_menu_list:
                    case 1:
                        print("Last call duration")
                    case 2:
                        print("All call duration")
                    case 3:
                        print("Recieved call duration")
                    case 4:
                        print("Dailed call duration")
                    case 5:
                        print("Clear timer")
                    case 0:
                        print("Back to call register")

            case 6:
                print("for Show Call Cost")
                show_call_cost_menu = """

                1  Test call cost
                2  All cost call
                3  Clear counter
                0 Back to call register

                Select option:
                """
                show_call_cost_menu_list = int(input(show_call_cost_menu))
                match show_call_cost_menu_list:
                    case 1:
                        print("Test call cost")
                    case 2:
                        print("All cost call")
                    case 3:
                        print("Clear counter")
                    case 0:
                        print("Back to call register")

            case 7:
                print("Call cost setting")
                call_cost_settings_menu = """

                1  Call cost limit
                2  show cost in
                0  Back to call register

                Select option:
                """

                call_cost_settings_menu_list = int(input(call_cost_settings_menu))
                match call_cost_settings_menu_list:
                    case 1:
                        print("Call cost limit")
                    case 2:
                        print("show cost in")
                    case 0:
                        print("Back to call register")

            case 8:
                print("Perpaid credit")
            case 0:
                print("Back to Nokia menu")

    case 5:
        print("Tones")
        tone_menu = """

        1  Ringing tone
        2  Ringing volume
        3  Incoming call alert
        4  composer
        5  Message alert tone
        6  Keypad tones
        7  Warning and game tones
        8  viberating alert
        9  screen saver
        0 Back to Nokia menu

        Select option:
        """

        tone_menu_list = int(input(tone_menu))
        match tone_menu_list:
            case 1:
                print("Ringing tone")
            case 2:
                print("Ringing volume")
            case 3:
                print("Incoming call alert")
            case 4:
                print("composer")
            case 5:
                print("Message alert tone")
            case 6:
                print("Keypad tones")
            case 7:
                print("Warning and game tones")
            case 8:
                print("viberating alert")
            case 9:
                print("screen saver")
            case 0:
                print("Back to Nokia menu")

    case 6:
        print("Settings")
        settings_menu = """

        1  Call settings
        2  Phone settings
        3  Security settings
        4  Restore factory settings
        0 Back to Nokia menu

        Select option:
        """

        settings_menu_list = int(input(settings_menu))
        match settings_menu_list:
            case 1:
                print("Call settings")
                call_settings_menu = """

                1 Automatic redial
                2 Speed dial
                3 Call waiting option
                4 Own number
                5 Phone in use
                6 Automatic answer
                0 Back to settings

                Select option:
                """
                call_settings_menu_list = int(input(call_settings_menu))
                match call_settings_menu_list:
                    case 1:
                        print("Automatic redial")
                    case 2:
                        print("Speed dial")
                    case 3:
                        print("Call waiting option")
                    case 4:
                        print("Own number")
                    case 5:
                        print("Phone in use")
                    case 6:
                        print("Automatic answer")
                    case 0:
                        print("Back to settings")

            case 2:
                print("Phone settings")
                phone_settings_menu = """

                1 Language
                2 call info display
                3 Welcome note
                4 Network selection
                5 Touch
                6 Confirm sim service action
                0 Back to settings

                Select option:
                """

                phone_settings_menu_list = int(input(phone_settings_menu))
                match phone_settings_menu_list:
                    case 1:
                        print("Language")
                    case 2:
                        print("call info display")
                    case 3:
                        print("Welcome note")
                    case 4:
                        print("Network selection")
                    case 5:
                        print("Touch")
                    case 6:
                        print("Confirm sim service action")
                    case 0:
                        print("Back to settings")

            case 3:
                print("Security settings")
                security_settings_menu = """

                1 Pin code request
                2 Call barring service
                3 Fix dialing
                4 Closed user group
                5 Phone security
                6 Change access code
                0 Back to settings

                Select option:
                """
                security_settings_menu_list = int(input(security_settings_menu))
                match security_settings_menu_list:
                    case 1:
                        print("Pin code request")
                    case 2:
                        print("Call barring service")
                    case 3:
                        print("Fix dialing")
                    case 4:
                        print("Closed user group")
                    case 5:
                        print("Phone security")
                    case 6:
                        print("Change access code")
                    case 0:
                        print("Back to settings")

            case 4:
                print("Restore factory settings")
            case 0:
                print("Back to Nokia menu")

    case 7:
        print("Call divert")

    case 8:
        print("Games")

    case 9:
        print("Calculator")

    case 10:
        print("Reminder")

    case 11:
        print("Clock")
        clock_menu = """

        1  Alarm clock
        2  Clock settings
        3  Date setting
        4  Stopwatch
        5  Countdown time
        6  Auto update date and time
        0 Back to Nokia menu

        Select option:
        """
        clock_menu_list = int(input(clock_menu))
        match clock_menu_list:
            case 1:
                print("Alarm clock")
            case 2:
                print("Clock settings")
            case 3:
                print("Date setting")
            case 4:
                print("Stopwatch")
            case 5:
                print("Countdown time")
            case 6:
                print("Auto update date and time")
            case 0:
                print("Back to Nokia menu")

    case 12:
        print("Profile")

    case 13:
        print("Sim service")