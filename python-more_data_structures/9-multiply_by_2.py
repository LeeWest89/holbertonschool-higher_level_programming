#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    m_dictionary = a_dictionary.copy()
    for key, value in m_dictionary.items():
        m_dictionary[key] = value * 2
    return (m_dictionary)
