import webapp2
import os
import jinja2
import json

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# all_ghosts = {
#     "Marilyn Monroe":{ "age":"21 to 40",
#                 "location": "North America",
#                 "hobby": "Acting",
#     },
#     "Emperor Hirito":{ "age":"41 to 100",
#                       "location":"Asia",
#                       "hobby":"Taking Care of Fish"
        
#     },
#     "William Shakespeare":{ "age":"18 to 20",
#                       "location":"Europe",
#                       "hobby":"Board Games"
#     }
# }

# all_ghosts = [
#     {
#     "name": "Marilyn Monroe",
#     "age": "18 to 20",
#     "location": "North America",
#     "hobby": "Acting",
#     },
#     {
#     "name": "Emperor Hirito",
#     "age": "41 to 100",
#     "location": "Asia",
#     "hobby": "Taking Care of Fish"
#     }
# ]



# def FindMatch(user_hobby, user_location, user_age):
#     name = all_ghosts
#     highest_score = 0
#     for ghost in all_ghosts:
#         temp_score= 0
#         if user_hobby == ghost['hobby']:
#             temp_score += 10
#         if ghost['location'] == user_location:
#             temp_score += 10
#         if ghost['age'] == user_age:
#             temp_score += 10
#         if temp_score > highest_score:
#             highest_score = temp_score 
#             name = ghost['name']
            
#     print(highest_score)
#     print(name)
        

class MatchFind(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/index.html")
        self.response.write(start_template.render())
        
    def post(self):
        user_location = self.request.get('Location')
        user_hobby = self.request.get('Hobby')
        user_age = self.request.get('Age')
        user_gender = self.request.get('Gender')
        
        # print ("Location: " + user_location)
        # print("Hobby: " + user_hobby)
        # print("Age: " + user_age)
        
        # name = FindMatch(user_hobby,user_location,user_age)
        
        myInput = {
        'location': user_location,
        'age': user_age,
        'hobby': user_hobby,
        'gender': user_gender
        }
        
        peopleList = [
          {
            'name': 'William Shakespeare',
            'location': 'Europe',
            'age': '39-58',
            'hobby': 'Playing_board_games',
            'gender': "Male",
            'summary': 'I was an important member of the Lord Chamberlains Men company of theatrical' + '\nplayers from roughly 1594 onward. Written records gave little indication of the way in which my professional life molded my artistry.' + '\nAll that can be deduced is that, in my 20 years as a playwright, I wrote plays that capture the complete range of human emotion and conflict.',
            'phone': "+7(777)433-3823",
            'url_': "https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg"
            },
          {
            'name': 'Leonardo da Vinci',
            'location': 'Europe',
            'age': '59-78',
            'hobby': 'Creating_inventions',
            'gender': "Male",
            'summary': 'With a curious mind and keen intellect, I studied the laws of science and nature,' + '\nwhich greatly informed my work. My ideas and body of work influenced countless artists and made me a leading light of the Italian Renaissance.',
            'phone': "+7(777)744-3534",
            'url_': "http://www.leonardodavinci.net/images/leonardo-da-vinci.jpg"
          },
          {
            'name': 'Napolean Bonaparte',
            'location': 'Europe',
            'age': '39-58',
            'hobby': 'Failing_to_capture_Russia',
            'gender': "Male",
            'summary': 'I was a military general and the first emperor of France and I am considered one of the worlds' + '\ngreatest military leaders. I revolutionized military organization and training, sponsored the Napoleonic Code, reorganized education,' +  '\nand established the long-lived Concordat with the papacy.',
            'phone': "+7(777)332-3532",
            'url_': "https://cdn.shopify.com/s/files/1/0895/0864/products/1344766_1024x1024.jpeg?v=1453563829"
          },
          {
            'name': 'Elvis Presley',
            'location': 'North_America',
            'age': '39-58',
            'hobby': 'Playing_music',
            'gender': "Male",
            'summary': 'I came from a very humble beginning and grew up to become one of the biggest names in rock n roll. By the mid-1950s, I appeared on the radio, television and the silver screen.',
            'phone': "+7(777)835-5342",
            'url_': "https://cdn.pastemagazine.com/www/articles/ForgottenElvisMain.jpg"
          },
          {
            'name': 'Marilyn Monroe',
            'location': 'North_America',
            'age': '18-38',
            'hobby': 'Acting',
            'gender': "Female",
            'summary': 'During my all-too-brief life, I overcame a difficult childhood to become one of the worlds biggest and most enduring sex symbols. During my career, my films earned more than $200 million',
            'phone': "+6(666)934-8923",
            'url_': "http://bizarreandgrotesque.files.wordpress.com/2015/08/marilyn.jpg"
          },
          {
            'name': 'Joan of Arc',
            'location': 'Europe',
            'age': '18-38',
            'hobby': 'Fighting',
            'gender': "Female",
            'summary': 'I was sent alongside French troops to the siege of Orleans and rose to prominence after the siege was lifted after nine days.' + '\nI was later captured and burned at the stake for heresy. However, as I predicted, seven years after my death, France was reunited with the English defeated and Charles crowned King.',
            'phone': "+7(777)433-383",
            'url_': "https://thumbs-prod.si-cdn.com/w_M02__RTd0rvTt4cmqpd1VYvck=/800x600/filters:no_upscale()/https://public-media.smithsonianmag.com/filer/a7/77/a777a064-2efe-4544-bea8-16b262aa43fc/joan_of_arc_on_horseback.jpg"
          },
          {
            'name': 'Emperor Hirohito',
            'location': 'Asia',
            'age': '79-98',
            'hobby': 'Taking_care_of_marine_life',
            'gender': "Male",
            'summary': 'I was Japans longest-reigning monarch, ruling from 1926 to 1989. The level of my involvement with Japans military during World War II has remained debatable, though I announced the countrys surrender to the Allied Forces in 1945.' + '\nAfter the war, the new constitution, drafted by the United States, transformed Japan into a constitutional monarchy so that sovereignty lay with the people instead of the emperor. I died in Tokyo on January 7, 1989. My son, Akihito, succeeded me.',
            'phone': "+6(666)724-2423",
            'url_': "https://historynewsnetwork.org/sites/default/files/159910-hrtoa.jpg"
          },
          {
            'name': 'Yao Beina',
            'location': 'Asia',
            'age': '18-38',
            'hobby': 'Singing',
            'gender': "Female",
            'summary': 'I was a chinese pop singer, known for singing the theme tune of TV drama The Legend of Zhen Huan. I died from breast cancer on Friday afternoon at the age of 33. Doctors found that the cancer cells had spread to my brain and lungs' + '\nthat I decided to donate my corneas before my death in 2013, I was a contestant on the Voice of China, singing contest and gained wide popularity. My death brought breast cancer to the fore again.',
            'phone': "+6(666)834-0833",
            'url_': "http://images.china.cn/attachement/jpg/site1007/20131226/0019b91ec74f1426198422.jpg"
          },
          {
            'name': 'Qin Shi Huang',
            'location': 'Asia',
            'age': '39-58',
            'hobby': 'Melting_people_in_tar',
            'gender': "Male",
            'summary': 'I was King of the state of Qin. During my lifetime, I conquered all the seven warring and diverging states, becoming the first person to unify China.' + '\nI took the title Emperor of the Qin dynasty and shaped the history of modern China.',
            'phone': "+6(666)893-2945",
            'url_': "https://cdn.britannica.com/700x450/24/102324-004-91E0F06A.jpg"
          },
          {
            'name': 'Frida Kahlo',
            'location': 'North_America',
            'age': '39-58',
            'hobby': 'Painting',
            'gender': "Female",
            'summary': 'I was considered one of Mexicos greatest artists who began painting mostly self-portraits after I was severely injured in a bus accident.' + '\nI later became politically active and married fellow communist artist Diego Rivera in 1929. I exhibited my paintings in Paris and Mexico before my death in 1954',
            'phone': "+7(777)823-0235",
            'url_': "https://www.biography.com/.image/t_share/MTQ4MzUzMTQxMDIzMTg4Mzk0/frida_kahlo_getty_images_451874162jpg.jpg"
          },
          {
            'name': 'Sun Tzu',
            'location': 'Asia',
            'age': '39-58',
            'hobby': 'Analyzing_how_to_win_war',
            'gender': "Male",
            'summary': 'I am believed to have written the famous ancient Chinese book on military strategy, The Art of War. Through my legends and the influential The Art of War, I had a significant impact on Chinese and Asian history and culture.',
            'phone': "+7(777)435-8230",
            'url_': "https://vignette.wikia.nocookie.net/highlander/images/1/11/Suntzu.png/revision/latest?cb=20160228194003"
          },
          {
            'name': 'Walt Disney',
            'location': 'North_America',
            'age': '59-78',
            'hobby': 'Making_cartoons',
            'gender': "Male",
            'summary': 'My brother and I co-founded Walt Disney Productions, which became one of the best-known motion-picture production companies in the world. I was an innovative animator and created the cartoon character Mickey Mouse.' + '\nI won 22 Academy Awards during my lifetime, and was the founder of theme parks Disneyland and Walt Disney World.',
            'phone': "+7(777)829-9021",
            'url_': "https://cfvod.kaltura.com/p/1034971/sp/103497100/thumbnail/entry_id/1_ne1z58vk/version/100021/width/640/height/360"
          }
          
        ]
        personPoints = []
        namesArray = []
        counter = 0
        for i in myInput:
            #myInput is location, age, hobby. Made from drop down.
            #i is the property
          print i + ": " + myInput[i]
          
          #myInput[i] is printing the values
          for person in peopleList:
              #person in peopleList is the individual dictionaries in peopleList
            print person
            print '------------------------'
            for personProps in person:
                #personProps in person is the properties in the individual dictionaries
              
              print person[personProps]
              # if person['name'] == 'Napolean Bonaparte':
                
              #   if i=='hobby':
              #     print "HHHOOOOOBBBBBYYYYYYY"
              #     print personProps
              #     print person[personProps]
                
              #     print '@ Shakespeare'
                  
              #     print i
              #     print myInput[i]
              #     exit()

              if person[personProps] == myInput[i]:
                # if counter <1:
                #   print "PRINTING CURRENT ITEM FOUND"
                #   print i
                #   counter+=1
                # else:
                #   exit()
                # if i == "hobby":
                #   print "MATCHED HOBBY!"
                #   exit()
                  #if the value of the individual dictionaries == myInput[i]
                if person['name'] not in namesArray:
                  print "did not find " + person['name']
                  namesArray.append(person['name'])
                  
                  num = 1
                  
                  #if person['name'] is not in namesArray append the name into namesArray, so it won't duplicate. Also set num to 1 for person.
                  
                  possibleSoulmate = {
                    'name': person['name'],
                    'num': num,
                    'why': [myInput[i]],
                    'location': person['location'],
                    'hobby': person['hobby'],
                    'age': person['age'],
                    'gender': person['gender'],
                    'summary': person['summary'],
                    'phone': person['phone'],
                    'url': person['url_']
                  }
                  #dictionary for personPoints array(their profile/ Their data)
                  
                  personPoints.append(possibleSoulmate)
                  #append the dictionary into personPoints array.
                else:
                    #This happens when name is already in namesArray
                  print "did find " + person['name']
                  for m in personPoints:
                    if m['name'] == person['name']:
                      m['num']+=1
                      m['why'].append(myInput[i])
                      #m is the profiles inside personPoints.
                      #we loop through personPoints to add +1
                      #we know who to add 1 to because we stop. Each stop has like a mini cycle it goes through, which in turn has more mini cycles.


        # print personPoints[0].num
        # print personPoints
        personPoints = sorted(personPoints, key=lambda x: x['num'], reverse=True)
        #lambda is sorting our array of dictionaries based on our num property

        print personPoints
        print personPoints[0]
        
        start_template=jinja_current_directory.get_template("templates/results.html")
        self.response.write(start_template.render(personPoints[0]))
        #we render personPoints[0] which is the highest scoring person because we sort via highest to lowest
# personPoints.sort(key=lambda x: x['num'], reverse=True)
class about(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_current_directory.get_template('templates/about.html')
        self.response.write(about_template.render())
        
class contact(webapp2.RequestHandler):
    def get(self):
        contact_template = jinja_current_directory.get_template('templates/contact.html')
        self.response.write(contact_template.render())
        
class home(webapp2.RequestHandler):
    def get(self):
        contact_template = jinja_current_directory.get_template('templates/index.html')
        self.response.write(contact_template.render())
        
class retry(webapp2.RequestHandler):
    def get(self):
        contact_template = jinja_current_directory.get_template('templates/index.html')
        self.response.write(contact_template.render())

# print namesArray
        
app = webapp2.WSGIApplication([
    ('/', MatchFind),
    ('/about', about),
    ('/contact', contact),
    ('/index', home, retry)
], debug=True)

start_template=jinja_current_directory.get_template