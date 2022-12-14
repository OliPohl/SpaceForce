using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    ####################################################
    #                   Boundaries.cs                  #
    #--------------------------------------------------#
    # This script makes stops the player from escaping #
    # the camera.                                      #
    ####################################################
*/  
public class BoundariesScript : MonoBehaviour
{
    private Vector2 ScreenBounds;

    private float ObjectWidth;
    private float ObjectHeight;
    

    void Start()
    {
        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.

        ObjectWidth = transform.GetComponent<CapsuleCollider2D>().bounds.size.x / 2;   // Gives half of the spaceships width.
        ObjectHeight = transform.GetComponent<CapsuleCollider2D>().bounds.size.y / 2;  // Gives half of the spaceships height.
    }

    
    void LateUpdate()   // This works because the update is after the normal update. The ViewPos is saved from last frame and inserted if its not in the range.
    {
        Vector3 ViewPos = transform.position; 
        ViewPos.x = Mathf.Clamp(ViewPos.x, ((ScreenBounds.x - ObjectWidth) * -1), (ScreenBounds.x - ObjectWidth));      // Gives back ViewPos.x if it is inside of the screen - Spaceship width.
        ViewPos.y = Mathf.Clamp(ViewPos.y, ((ScreenBounds.y - ObjectHeight) * -1), (ScreenBounds.y - ObjectHeight));    // Gives back ViewPos.y if it is inside of the screen - Spaceship height.
        transform.position = ViewPos;   // Updates the Position. 
    }
}
