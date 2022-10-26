# UTF-8.







import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
PI = 3.14159265359



def move_base_to(x, y):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while (not client.wait_for_server(rospy.Duration(5))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    if x == 0.0263 and y == -0.0915:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.005
        goal.target_pose.pose.orientation.w = 1.000

    #(if x == 0.467 and y == -0.142:
        #goal.target_pose.pose.orientation.x = 0.0
        #goal.target_pose.pose.orientation.y = 0.0
        #goal.target_pose.pose.orientation.z = -0.652
        #goal.target_pose.pose.orientation.w = 0.758)
    #if x ==  0.410 and y == -0.480:
        #goal.target_pose.pose.orientation.x = 0.0
        #goal.target_pose.pose.orientation.y = 0.0
        #goal.target_pose.pose.orientation.z = -0.725
        #goal.target_pose.pose.orientation.w = 0.689
    if x ==  0.458 and y == -1.699:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -1.000
        goal.target_pose.pose.orientation.w = 0.0268
    #if x == -0.073 and y == -1.723:
        #goal.target_pose.pose.orientation.x = 0.0
        #goal.target_pose.pose.orientation.y = 0.0
        #goal.target_pose.pose.orientation.z = 0.713
        #goal.target_pose.pose.orientation.w = 0.701
    if x == -0.055 and y == -0.486:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -1.000
        goal.target_pose.pose.orientation.w = 0.005
    #if x == -0.607 and y == -0.495:
        #goal.target_pose.pose.orientation.x = 0.0
        #goal.target_pose.pose.orientation.y = 0.0
        #goal.target_pose.pose.orientation.z = -0.690
        #goal.target_pose.pose.orientation.w = 0.724
    if x == -0.735 and y == -2.170:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.713
        goal.target_pose.pose.orientation.w = 0.702
    #goal.target_pose.pose.orientation.x = 0.0
    #goal.target_pose.pose.orientation.y = 0.0
    #goal.target_pose.pose.orientation.z = 0.708
    #goal.target_pose.pose.orientation.w = 1.0
    rospy.loginfo("Sending goal")
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available")
    else:
        return client.get_result()



if __name__ == '__main__':
    goal_positions =[[0.0263, -0.0915],
                    #[0.467,  -0.142],
                    #[0.410, -0.480],
                    [0.458,   -1.699],
                    #[-0.073,  -1.723],
                    [-0.055,   -0.486],
                    #[-0.607, -0.495],
                    [ -0.735, -2.170]]
    rospy.init_node("set_navigation_goal")

    for x, y in goal_positions:
        result = move_base_to(x, y)
        if result:
            continue
        else:
            rospy.loginfo("The move_base failed to get to goal for some reasons")
            break
        rospy.logininfo("Good job!!!")
