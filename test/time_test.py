import unittest
import pygame
import time

Clock = pygame.time.Clock


class ClockTypeTest(unittest.TestCase):
    def test_construction(self):
        """Ensure a Clock object can be created"""
        c = Clock()

        self.assertTrue(c, "Clock cannot be constructed")

    def todo_test_get_fps(self):

        # __doc__ (as of 2008-08-02) for pygame.time.Clock.get_fps:

        # Clock.get_fps(): return float
        # compute the clock framerate
        #
        # Compute your game's framerate (in frames per second). It is computed
        # by averaging the last few calls to Clock.tick().
        #

        self.fail()

        # delay_per_frame = 1 / 100.0
        #
        # c = Clock()
        #
        # for f in range(100):
        #     c.tick()
        #     time.sleep(delay_per_frame)
        #
        # self.assertTrue(99.0 < c.get_fps() < 101.0)

    def todo_test_get_rawtime(self):

        # __doc__ (as of 2008-08-02) for pygame.time.Clock.get_rawtime:

        # Clock.get_rawtime(): return milliseconds
        # actual time used in the previous tick
        #
        # Similar to Clock.get_time(), but this does not include any time used
        # while Clock.tick() was delaying to limit the framerate.
        #

        self.fail()

    def test_get_time(self):
        #Testing parameters
        delay = 0.1 #seconds
        delay_miliseconds = delay*(10**3)
        iterations = 10
        delta = 50 #milliseconds

        #Testing Clock Initialization
        c = Clock()
        self.assertEqual(c.get_time(), 0)

        #Testing within delay parameter range
        for i in range(iterations):
            time.sleep(delay)
            c.tick()
            c1 = c.get_time()
            self.assertAlmostEqual(delay_miliseconds, c1, delta=delta)

        #Comparing get_time() results with the 'time' module
        for i in range(iterations):
            t0 = time.time()
            time.sleep(delay)
            c.tick() 
            t1 = time.time()
            c1 = c.get_time() #elapsed time in milliseconds
            d0 = (t1-t0)*(10**3) #'time' module elapsed time converted to milliseconds
            self.assertAlmostEqual(d0, c1, delta=delta)

    def todo_test_tick(self):

        # __doc__ (as of 2008-08-02) for pygame.time.Clock.tick:

        # Clock.tick(framerate=0): return milliseconds
        # control timer events
        # update the clock
        #
        # This method should be called once per frame. It will compute how
        # many milliseconds have passed since the previous call.
        #
        # If you pass the optional framerate argument the function will delay
        # to keep the game running slower than the given ticks per second.
        # This can be used to help limit the runtime speed of a game. By
        # calling Clock.tick(40) once per frame, the program will never run at
        # more than 40 frames per second.
        #
        # Note that this function uses SDL_Delay function which is not
        # accurate on every platform, but does not use much cpu.  Use
        # tick_busy_loop if you want an accurate timer, and don't mind chewing
        # cpu.
        #

        self.fail()

        # collection = []
        # c = Clock()
        #
        # c.tick()
        # for i in range(100):
        #     time.sleep(0.005)
        #     collection.append(c.tick())
        #
        # for outlier in [min(collection), max(collection)]:
        #     if outlier != 5: collection.remove(outlier)
        #
        # self.assertEqual(sum(collection) / len(collection), 5)

    def todo_test_tick_busy_loop(self):

        # __doc__ (as of 2008-08-02) for pygame.time.Clock.tick_busy_loop:

        # Clock.tick_busy_loop(framerate=0): return milliseconds
        # control timer events
        # update the clock
        #
        # This method should be called once per frame. It will compute how
        # many milliseconds have passed since the previous call.
        #
        # If you pass the optional framerate argument the function will delay
        # to keep the game running slower than the given ticks per second.
        # This can be used to help limit the runtime speed of a game. By
        # calling Clock.tick(40) once per frame, the program will never run at
        # more than 40 frames per second.
        #
        # Note that this function uses pygame.time.delay, which uses lots of
        # cpu in a busy loop to make sure that timing is more accurate.
        #
        # New in pygame 1.8.0.

        self.fail()

class TimeModuleTest(unittest.TestCase):
    def test_delay(self):
        """Tests time.delay() function."""
        millis = 50  # millisecond to wait on each iteration
        iterations = 20  # number of iterations
        delta = 50  # Represents acceptable margin of error for wait in ms
        # Call checking function
        self._wait_delay_check(pygame.time.delay, millis, iterations, delta)
        # After timing behaviour, check argument type exceptions
        self._type_error_checks(pygame.time.delay)

    def test_get_ticks(self):
        """Tests time.get_ticks()"""
        """
         Iterates and delays for arbitrary amount of time for each iteration,
         check get_ticks to equal correct gap time
        """
        iterations = 20
        millis = 50
        delta = 15  # Acceptable margin of error in ms
        # Assert return type to be int
        self.assertTrue(type(pygame.time.get_ticks()) == int)
        for i in range(iterations):
            curr_ticks = pygame.time.get_ticks()  # Save current tick count
            curr_time = time.time()  # Save current time
            pygame.time.delay(millis)  # Delay for millis
            # Time and Ticks difference from start of the iteration
            time_diff = round((time.time() - curr_time)*1000)
            ticks_diff = pygame.time.get_ticks() - curr_ticks
            # Assert almost equality of the ticking time and time difference
            self.assertAlmostEqual(ticks_diff, time_diff, delta=delta)

    def test_set_timer(self):
        """Tests time.set_timer()"""
        """
        Tests if a timer will post the correct amount of eventid events in
        the specified delay.
        Also tests if setting milliseconds to 0 stops the timer and if
        the once argument works.
        """
        pygame.display.init()
        TIMER_EVENT_TYPE = pygame.event.custom_type()
        timer_event = pygame.event.Event(TIMER_EVENT_TYPE, {'code': 0})
        delta = 200
        timer_delay = 250
        test_number = 8 # Number of events to read for the test
        events = 0 # Events read
        pygame.time.set_timer(TIMER_EVENT_TYPE, timer_delay)

        # Test that 'test_number' events are posted in the right amount of time
        t1 = pygame.time.get_ticks()
        max_test_time = t1 + timer_delay * test_number + delta
        while events < test_number:
            for event in pygame.event.get():
                if event == timer_event:
                    events += 1
            # The test takes too much time
            if pygame.time.get_ticks() > max_test_time:
                break
        pygame.time.set_timer(TIMER_EVENT_TYPE, 0)
        t2 = pygame.time.get_ticks()
        # Is the number ef events and the timing right?
        self.assertEqual(events, test_number)
        self.assertAlmostEqual(timer_delay * test_number, t2-t1, delta=delta)

        # Test that the timer stoped when set with 0ms delay.
        pygame.event.get()
        pygame.time.delay(500)
        self.assertNotIn(timer_event, pygame.event.get())

        # Test that the once argument works
        pygame.time.set_timer(TIMER_EVENT_TYPE, 10, True)
        pygame.time.delay(100)
        self.assertEqual(pygame.event.get().count(timer_event), 1)

    def test_wait(self):
        """Tests time.wait() function."""
        millis = 100  # millisecond to wait on each iteration
        iterations = 10  # number of iterations
        delta = 50  # Represents acceptable margin of error for wait in ms
        # Call checking function
        self._wait_delay_check(pygame.time.wait, millis, iterations, delta)
        # After timing behaviour, check argument type exceptions
        self._type_error_checks(pygame.time.wait)

    def _wait_delay_check(self, func_to_check, millis, iterations, delta):
        """"
         call func_to_check(millis) "iterations" times and check each time if
         function "waited" for given millisecond (+- delta). At the end, take
         average time for each call (whole_duration/iterations), which should
         be equal to millis (+- delta - acceptable margin of error).
         *Created to avoid code duplication during delay and wait tests
        """
        # take starting time for duration calculation
        start_time = time.time()
        for i in range(iterations):
            wait_time = func_to_check(millis)
            # Check equality of wait_time and millis with margin of error delta
            self.assertAlmostEqual(wait_time, millis, delta=delta)
        stop_time = time.time()
        # Cycle duration in millisecond
        duration = round((stop_time-start_time)*1000)
        # Duration/Iterations should be (almost) equal to predefined millis
        self.assertAlmostEqual(duration/iterations, millis, delta=delta)

    def _type_error_checks(self, func_to_check):
        """Checks 3 TypeError (float, tuple, string) for the func_to_check"""
        """Intended for time.delay and time.wait functions"""
        # Those methods throw no exceptions on negative integers
        self.assertRaises(TypeError, func_to_check, 0.1)  # check float
        self.assertRaises(TypeError, pygame.time.delay, (0, 1))  # check tuple
        self.assertRaises(TypeError, pygame.time.delay, "10")  # check string

###############################################################################

if __name__ == "__main__":
    unittest.main()
