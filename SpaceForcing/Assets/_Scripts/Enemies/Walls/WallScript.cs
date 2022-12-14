using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WallScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] private ColorSettings ColorSettings;

    [SerializeField] private GameObject WallTop;
    [SerializeField] private GameObject Gate;
    [SerializeField] private GameObject WallBot;


    // Screen Catching
    private Vector2 ScreenBounds;
    private float ObjectWidth;
    private float ObjectHeight;


    // General Variables
    Vector3 NextPosWallTop, NextPosWallBot, NextPosGate; 
    private Material GateMaterial;
    private int Health;
    // private bool BobbingUp;
    // private float NextBob = 0.0f;


    // [SerializeField] public bool isBobbing;   // Replace these by GameMaster.


    void Start()
    {
        GateMaterial = Gate.GetComponent<Renderer>().material;   // Gets the material of the gate

        Health = Random.Range(1, GameSettings.GateMaxHealth+1);

        // ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.

        // ObjectWidth = transform.GetComponent<CapsuleCollider2D>().bounds.size.x / 2;   // Gives half of the wall width.
        // ObjectHeight = transform.GetComponent<CapsuleCollider2D>().bounds.size.y / 2;  // Gives half of the wall height.

        // BobbingUp = Random.Range(0,2) == 1;
    }

    
    void Update()
    {
        Move();
        UpdateHealth();
    }


    private void Move()
    {
        Vector3 TempVect = new Vector3(-1, 0, 0); 

        TempVect = TempVect.normalized * Time.deltaTime * GameSettings.WallSpeed * 7;

        NextPosWallTop = WallTop.transform.position + TempVect;
        NextPosWallBot = WallBot.transform.position + TempVect;
        NextPosGate = Gate.transform.position + TempVect;
        // if (isBobbing){Bobbing();}  // if bobbing add the new y to the nextPosition

        transform.position = NextPosWallTop;
        WallTop.transform.position = NextPosWallTop;
        WallBot.transform.position = NextPosWallBot;
        Gate.transform.position = NextPosGate;
    }


    // private void Bobbing()  // Bobbes the cube up and down if activated
    // { 
    //     if (BobbingUp)
    //     {
    //         NextPos.y = Mathf.Clamp(NextPos.y + 0.05f, ((ScreenBounds.y - ObjectHeight) * -1), (ScreenBounds.y - ObjectHeight));

    //         if (Time.time > NextBob)
    //             {
    //             NextBob = Time.time + ((GameSettings.BobbingHeight * 2) / 7); 
    //             BobbingUp = false;
    //             }
    //     }
    //     else
    //     {
    //         NextPos.y = Mathf.Clamp(NextPos.y - 0.05f, ((ScreenBounds.y - ObjectHeight) * -1), (ScreenBounds.y - ObjectHeight));

    //         if (Time.time > NextBob)
    //             {
    //             NextBob = Time.time + ((GameSettings.BobbingHeight * 2) / 7); 
    //             BobbingUp = true;
    //             }
    //     }
    // }


    private void UpdateHealth() // changes cube color to current health, color in ColorSettings
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


    void OnBecameInvisible() // Destroy wall if out of screen
    {   
        Debug.Log("Hey");
        Destroy(this);
    }
}