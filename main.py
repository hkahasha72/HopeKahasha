import random
import time
import threading

def countdown ():
    global my_timer

    my_timer = 5 

    for x in range (5):
        my_timer = my_timer - 1 
        sleep (1)

    print ("Times up!")


# This Section is the Defined, questions + answers for the driver's test, plus the hints 
questions = [
    {
        'question': 'You are in a crash. The police are not in attendance. Someone is injured. What should you do?',
        'options': ['A: Make sure the injured person is alright then drive on', 'B: Report the crash to the nearest open police station', 'C: Report the crash to the nearest open police station if property has also been damaged'],
        'answer': 'B',
        'hint': 'it requires imediate action'
    },
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'When is vehicle A allowed to turn right?',
        'options': ['A: Before vehicle B turns right', 'B: After vehicle B has turned right ','C: Vehicle A is not allowed to turn right.'],
        'answer': 'A',
        'hint': 'Using a hands-free system allows you to communicate safely while driving.'
    },
    {
        'question': 'You want to park your vehicle. You must NOT park within 20 metres either side of',
        'options': ['A: an intersection with traffic lights.', 'B: a safety zone.', 'C: a traffic island'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'You are driving on a multi-lane freeway. There are no transit lanes. When are you allowed to drive in the right lane?',
        'options': ['A: Only to overtake or when the road is congested', 'B: Only if you are travelling at the speed limit', 'C: At any time'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'A tram stops ahead of your vehicle. Pedestrians get off the tram and wait to cross in front of you. You must stop',
        'options': ['A: level with the drivers door', 'B: level with the rear of the tram', 'C: level with the rear door.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'David is a P1 driver. He wants to use the GPS navigation system in his car. What must he do to reduce the risk of crashing?',
        'options': ['A: Turn off the GPS sound and rely only on the images.', 'B: Program the GPS before starting his journey. ', 'C: Keep the GPS on his lap and use voice controls so he does not have to reach for it while driving.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    }, 
    {
        'question': 'The outside mirrors of your car should be adjusted so that a part of the mirror shows',
        'options': ['A: your reflection.', 'B: the inside of your car.', 'C: the edge of your car.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'Your licence has been cancelled. You are...',
        'options': ['A: not allowed to drive under any circumstances', 'B: allowed to drive only in an emergency', 'C: allowed to drive to work if there is no other type of transport available.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'You are driving while very tired. You suddenly realise you cannot remember the last few kilometres of road. You should',
        'options': ['A: open a window and keep driving', 'B: drive faster to frighten yourself into staying awake.', 'C: pull over and sleep.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'You are entering a lane of traffic from the side of the road. How long must you signal with your indicators before you pull out?',
        'options': ['A: Up to 2 seconds', 'B: At least 5 seconds', 'C: More than 10 seconds'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'Janelle has a P1 probationary licence. She pulls over to the side of the road but does not park her car. What is she NOT allowed to do?',
        'options': ['A: Listen to music from the cars stereo.', 'B: Talk to a passenger in the back seat.', 'C: Make a call on a hands free mobile phone.'],
        'answer': 'B',
        'hint': 'it requires imediate action'
    },
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'Why is it important to scan the road scene when you drive?',
        'options': ['A: It will help you stay awake.', 'B: You are more likely to anticipate potential hazards.','C: You will develop good vehicle control.'],
        'answer': 'A',
        'hint': 'Using a hands-free system allows you to communicate safely while driving.'
    },
    {
        'question': 'You are approaching a railway crossing. A railway employee is signalling you to stop. You cannot see any trains coming. What should you do?',
        'options': ['A: Stop.', 'B: Slow down and drive carefully across.', 'C: Sound your horn and drive across as quickly as possible.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'When is the surface of a sealed road likely to be most slippery?',
        'options': ['A: When it has not rained for weeks', 'B: When it begins to rain', 'C: After several hours of rain'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'What is the speed limit on roads without speed limit signs outside built-up areas in Victoria?',
        'options': ['A: 60 km/h', 'B: 80 km/h', 'C: 100 km/h'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'In which of these situations are you allowed to drive in a bus lane?',
        'options': ['A: When you plan to turn left in less than 100 metres', 'B: When the traffic in other lanes has stopped moving', 'C: When making a three point turn'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    }, 
    {
        'question': 'You are driving at 100 km/h. What distance are you most likely to cover before you can stop?',
        'options': ['A: 40 metres', 'B: 80 metres', 'C: 140 metres'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'If you have a tyre blowout, you should',
        'options': ['A: immediately pull up the hand brake.', 'B: make sure the car is under control before using the brakes.', 'C: take your hands off the steering wheel and allow the car to slow down.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'How should you drive out of a bend in the road?',
        'options': ['A: Accelerate a little', 'B: Slow down a little', 'C: Continue at the same speed'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'Learner drivers with 120 hours of practice decrease their risk of crashing after they get their licence compared to drivers who have less practice. How much is the risk decreased?',
        'options': ['A: 10%', 'B: 20%', 'C: 30%'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'When you encounter a RED Stop sign at an intersection, what must you do?',
        'options': ['A: Slow down', 'B: Proceed at the speed limit', 'C: Come to a complete stop'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'What should be the main aim of a learner driver?',
        'options': ['A: To pass their licence test', 'B: To drive consistently with no mistakes ','C: 	To take their licence test after less than ten lessons'],
        'answer': 'B',
        'hint': 'Using a hands-free system allows you to communicate safely while driving.'
    },
    {
        'question': 'When entering a roundabout you must give way to',
        'options': ['A: All vehicles in the roundabout to your right only.', 'B: all vehicles in the roundabout to your left only.', 'C: All vehicles already in the roundabout.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'You are travelling at 50 km/h on a dry road. It takes 35 metres to stop. What happens when the road is wet?',
        'options': ['A: You need more than 35 metres to stop.', 'B: You need less than 35 metres to stop.', 'C: The weather conditions do not affect the braking distance.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'Speeding increases the risk of a crash because it...',
        'options': ['A: Slows your reflexes.', 'B: Increases the number of road hazards.', 'C: Reduces the time for scanning the driving situation.'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'B',
        'hint': 'Its implied on the sign'
    }, 
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
]

def run_driver_test():
    score = 0
    total_questions = len(questions)
    incorrect_answers = []

    print ('Welcome to LetsDrive! the VIC Drivers Learner Test Practice app!, Input your name to start')
    my_name = input()
    print('Hello,' + my_name + ', today youll be taking a practice drivers test which will help you prepare for the real thing, you will have 25 minutes to complete this test and must answer at least 26 out of the 32 questions correctly ')
    print("Let's begin!\n")

    # Gives reader time to read the description before the test starts
    time.sleep(10)


    # option which Shuffles the questions
    random.shuffle(questions)

    # Iterate through the questions
    for question in questions:
        print(question['question'])
        for option in question['options']:
            print(option)
        user_answer = input("Enter your answer as so A, B or C: ").strip().upper()

        # Check the answer
        if user_answer == question['answer'].upper():
            score += 1
        else:
            incorrect_answers.append(question)

        print()

    # Calculate the passing score
    passing_score = int(0.8 * total_questions)

    print("Test complete!")
    print("Score:", score, "/", total_questions)

    if score >= passing_score:
        print("Congratulations! You passed the driver's test!")
    else:
        print("Unfortunately, you did not pass the driver's test.")
        print("Here are the questions you answered incorrectly:")
        for i, question in enumerate(incorrect_answers):
            print(f"\nQuestion {i+1}:")
            print(question['question'])
            print("Correct Answer:", question['answer'])
            

run_driver_test()

