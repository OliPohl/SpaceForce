using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*  
    ####################################################
    #               BackgroundScript.cs                #
    #--------------------------------------------------#
    # This script moves the background to the left and #
    # repeats it indefinetly.                          #
    # Speed is given in: GameSettings.cs               #
    ####################################################
*/  

public class BackgroundScript : MonoBehaviour
{
    [SerializeField] public GameSettings GameSettings;
    [SerializeField] public GameObject Water0, Water1, Water2, Water3, Water4;
    [SerializeField] public GameObject Sky0, Sky1, Sky2, Sky3, Sky4;


    private Vector3 WaterStartPos, SkyStartPos;
    private float WaterEndPosX, SkyEndPosX;


    void Start()    // Getting starting position of Water/Sky Nr.4 to reset them when they get to position 0.
    {
        WaterStartPos = Water4.transform.position;
        SkyStartPos = Sky4.transform.position;

        WaterEndPosX = Water0.transform.position.x;     // Water0/Sky0 are just here to get the ending position. We dont need them anymore.
        Destroy(Water0);
        SkyEndPosX = Sky0.transform.position.x;
        Destroy(Sky0);
        
    }


    void Update()   
    {               
        Move(Water1, true);         // Move(Object Name, is Water = true/ is Sky = false).
        Move(Water2, true);
        Move(Water3, true);
        Move(Water4, true);

        Move(Sky1, false);
        Move(Sky2, false);
        Move(Sky3, false);
        Move(Sky4, false);
    }


    private void Move(GameObject Object, bool Water) 
    {
        if (Water == true) // If its Water
        {

            if (Object.transform.position.x <= WaterEndPosX) // Checks if it has reached the end
            {
                Object.transform.position = WaterStartPos;  // Resets to in Start saved Position of Water4
            }
            else
            {
                Object.transform.position -= new Vector3(GameSettings.WaterSpeed / 150, 0, 0);    // Moves the Water to the left in the Speed set in GameSettings
            }
        }
        else // If its Sky
        {
            if (Object.transform.position.x <= WaterEndPosX) // Checks if it has reached the end
            {
                Object.transform.position = SkyStartPos; // Resets to in Start saved Position of Sky4
            }
            else
            {
                Object.transform.position -= new Vector3(GameSettings.SkySpeed / 150, 0, 0); // Moves the Sky to the left in the Speed set in GameSettings
            }
        }

    }
}
