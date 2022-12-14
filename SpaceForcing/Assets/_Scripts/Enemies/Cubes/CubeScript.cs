using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    ####################################################
    #                    CubeScript.cs                 #
    #--------------------------------------------------#
    # This script makes the cubes go to the left.      #
    # It updates their color based on hp left          #
    # You are abele to make them bobb if isBobbing     #
    #                                                  #
    # Speed/Health is given in: GameSettings.cs        #
    # Color is given in: ColorSettings.cs              #
    ####################################################
*/ 
public class CubeScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] private ColorSettings ColorSettings;

    // General
    private Rigidbody2D CubeRigidbody;
    private Material CubeMaterial;
    private int Health;
    private Vector3 NextPos;

    // Bobbing
    private Vector2 ScreenBounds;
    private float ObjectWidth;
    private float ObjectHeight;

    private bool BobbingUp;
    private float NextBob = 0.0f;
    
    // Change Later
    [SerializeField] public bool isBobbing;   // Replace these by GameMaster
    
    void Start()
    {
        CubeRigidbody = GetComponent<Rigidbody2D>();  // Gets the rigidbody of the cube
        CubeMaterial = GetComponent<Renderer>().material;   // Gets the material of the cube
        if (CubeRigidbody == null)
        {
            Debug.LogError("Cube is missing a Rigidbody component");
        }

        Health = Random.Range(1, GameSettings.CubeMaxHealth+1);

        if (isBobbing)  // tages screen size and randomizes the starting bobbS
        { 
            ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.
            ObjectHeight = transform.GetComponent<SpriteRenderer>().bounds.size.y / 2;  // Gives half of the cube height.

            BobbingUp = Random.Range(0,2) == 1;
        }
    }

    
    void Update()
    {
        Move();
        UpdateHealth();
    }
    


    private void Move()
    {
        Vector3 TempVect = new Vector3(-1, 0, 0);   // Makes a temp vecotor that will be added to the current positon of the cube. "* Time.deltaTime" makes it so that it it frames(10 frames per CubeSpeed)
        TempVect = TempVect.normalized * Time.deltaTime * GameSettings.CubeSpeed * 7;      

        NextPos = transform.position + TempVect;
        if (isBobbing){Bobbing();}  // if bobbing add the new y to the nextPosition

        CubeRigidbody.MovePosition(NextPos);
    }


    private void Bobbing()  // Bobbes the cube up and down if activated
    { 
        if (BobbingUp)
        {
            NextPos.y = Mathf.Clamp(NextPos.y + 0.05f, ((ScreenBounds.y - ObjectHeight) * -1), (ScreenBounds.y - ObjectHeight));

            if (Time.time > NextBob)
                {
                NextBob = Time.time + ((GameSettings.CubeBobbingHeight * 2) / 7); 
                BobbingUp = false;
                }
        }
        else
        {
            NextPos.y = Mathf.Clamp(NextPos.y - 0.05f, ((ScreenBounds.y - ObjectHeight) * -1), (ScreenBounds.y - ObjectHeight));

            if (Time.time > NextBob)
                {
                NextBob = Time.time + ((GameSettings.CubeBobbingHeight * 2) / 7); 
                BobbingUp = true;
                }
        }
    }


    private void UpdateHealth() // changes cube color to current health, color in ColorSettings
    {   
        switch(Health) 
        {
        case 1:
            CubeMaterial.color = ColorSettings.Hp1;
            break;
        case 2:
            CubeMaterial.color = ColorSettings.Hp2;
            break;
        case 3:
            CubeMaterial.color = ColorSettings.Hp3;
            break;
        case 4:
            CubeMaterial.color = ColorSettings.Hp4;
            break;
        case 5:
            CubeMaterial.color = ColorSettings.Hp5;
            break;
        case 6:
            CubeMaterial.color = ColorSettings.Hp6;
            break;
        case 7:
            CubeMaterial.color = ColorSettings.Hp7;
            break;
        case 8:
            CubeMaterial.color = ColorSettings.Hp8;
            break;
        case 9:
            CubeMaterial.color = ColorSettings.Hp9;
            break;
        case 10:
            CubeMaterial.color = ColorSettings.Hp10;
            break;
        default:
            Destroy(gameObject);
            break;
        }
    }


    void OnBecameInvisible() // Destroy cube if out of screen
    {
        Destroy(gameObject);
    }
}
