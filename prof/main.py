# UTF-8.
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
PI = 3.14159265359
def move_base_to(x,y):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while (not client.wait_for_server(rospy.Duration(5))):
        rospy.loginfo("Waiting for the move_base action server to come up")
    goal = MoveBaseGoal
    goal.target_pose.header.frame_id = "map"

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 0.0
    rospy.loginfo("Sending goal")
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
    else
        return client.get_result()



if __name__ == '__main__':
    goal_positions=[[1.00, 2.90],
                    [-6.55, -2.80]
                    [-1.35,  3.90]
                    [ 5.85, -4.65]
                    [ 6.45,  4.20]
                    [ 1.00,  1.90]]
    rospy.init_noe("set_navigation_goal")

    for x,y in goal_positions
        result = move_base_to(x,y)
        if result:
            continue
        else
            rospy.loginfo("The move_base failed to get to goal for some reasons")
            break
        rospy.logininfo("Good job!!!")





