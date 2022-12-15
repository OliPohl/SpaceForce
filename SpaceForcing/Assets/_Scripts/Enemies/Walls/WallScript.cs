using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    ####################################################
    #                    WallScript.cs                 #
    #--------------------------------------------------#
    # This script makes the walls go to the left.      #
    # It updates gates color based on hp left          #
    # You are abele to make them bobb if isBobbing.    #
    #                                                  #
    # Speed/Health is given in: GameSettings.cs        #
    # Color is given in: ColorSettings.cs              #
    ####################################################
*/
public class WallScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] private ColorSettings ColorSettings;

    [SerializeField] private GameObject Gate;


    // Screen Catching
    private Vector2 ScreenBounds;
    private float ObjectWidth;
    private float ObjectHeight;


    // General Variables
    Vector3 NextPos; 
    private Material GateMaterial;
    private int Health;
    private bool BobbingUp;
    private float NextBob = 0.0f;

    [SerializeField] public bool isBobbing;   // Replace these by GameMaster.


    void Start()
    {
        GateMaterial = Gate.GetComponent<Renderer>().material;   // Gets the material of the gate

        Health = Random.Range(1, GameSettings.GateMaxHealth+1);

        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.
        
        BobbingUp = Random.Range(0,2) == 1;
    }

    
    void Update()
    {
        Move();
        UpdateHealth();
        RemoveOnInvisible();
    }


    private void Move() // Moves Walls to the left
    {
        Vector3 TempVect = new Vector3(-1, 0, 0); 

        TempVect = TempVect.normalized * Time.deltaTime * GameSettings.WallSpeed;
        NextPos = transform.position + TempVect;

        if (isBobbing){Bobbing();}  // if bobbing add the new y to the nextPositions
        transform.position = NextPos;
    }


    private void Bobbing()  // Bobbes the walls up and down if activated
    { 
        float x = 0.01f;

        if (BobbingUp)
        {
            NextPos.y = Mathf.Clamp(NextPos.y + x, -5, 5); // need to use -5,5 because of fuckery

            if (Time.time > NextBob)
                {
                NextBob = Time.time + ((GameSettings.WallBobbingHeight * 2) / 7); 
                BobbingUp = false;
                }
        }
        else
        {
            NextPos.y = Mathf.Clamp(NextPos.y - x, -5, 5);

            if (Time.time > NextBob)
                {
                NextBob = Time.time + ((GameSettings.WallBobbingHeight * 2) / 7); 
                BobbingUp = true;
                }
        }
    }


    private void UpdateHealth() // changes gate color to current health, color in ColorSettings
    {   
        switch(Health) 
        {
        case 1:
            GateMaterial.color = ColorSettings.Hp1;
            break;
        case 2:
            GateMaterial.color = ColorSettings.Hp2;
            break;
        case 3:
            GateMaterial.color = ColorSettings.Hp3;
            break;
        case 4:
            GateMaterial.color = ColorSettings.Hp4;
            break;
        case 5:
            GateMaterial.color = ColorSettings.Hp5;
            break;
        case 6:
            GateMaterial.color = ColorSettings.Hp6;
            break;
        case 7:
            GateMaterial.color = ColorSettings.Hp7;
            break;
        case 8:
            GateMaterial.color = ColorSettings.Hp8;
            break;
        case 9:
            GateMaterial.color = ColorSettings.Hp9;
            break;
        case 10:
            GateMaterial.color = ColorSettings.Hp10;
            break;
        default:
            Destroy(gameObject);
            break;
        }
    }

    private void RemoveOnInvisible() // Destroy walls if out of screen, idk why i couldnt use the build in function but there you go.
    {   
        if (NextPos.x <= (ScreenBounds.x * -2))
            {
                Debug.Log("sdlfk");
                Destroy(gameObject);
            }
    }
}