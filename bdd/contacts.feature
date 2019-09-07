Scenario Outline: Add new contact
 Given a contact list
 Given a new contact with <firstname>, <lastname>, <address> and <homephone>
 When I add the contact to the list
 Then the new contact list is equal to the old list with the added contact

 Examples:
 | firstname  | lastname  | address  | homephone  |
 | Иван | Иванов | Москва | 3221110 |
 | Петр | Петров | Питер | 0123456 |

Scenario: Delete a contact
 Given a non-empty contact list
 Given an index of random contact from the list
 When I delete the contact from the list
 Then the new contact list is equal to the old list without the deleted contact