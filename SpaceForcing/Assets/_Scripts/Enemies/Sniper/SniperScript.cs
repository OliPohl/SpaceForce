using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    #####################################################
    #                 SniperScript.cs                   #
    #---------------------------------------------------#
    # This script Intros and Outros(when Spawner hidden)#
    # the snipers and makes them pick a random pos      #
    # makes them move to it while aiming and then fires #
    #                                                   #
    # Aiming Stats are given in: GameSettings.cs        #
    #####################################################
*/  
public class SniperScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;

    [SerializeField] private GameObject SniperLeft;
    [SerializeField] private GameObject SniperRight;
    [SerializeField] private GameObject BeamHighlight;
    [SerializeField] private GameObject BeamAttack;


    private Vector2 ScreenBounds;
    private float SniperWidth;
    private Vector3 SniperLeftPos;
    private GameObject SniperSpawner;
    private float AnimationSpeed = 0.005f;

    private bool Intro = true;
    private bool Outro = false;

    private float NextAim = 0.0f;
    private int Count = -1;
    private bool Aiming = true;
    private float MinPos, MaxPos, NextPos = 0.0f;


    void Start()
    {
        Debug.Log("pos" +transform.position);
        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.localPosition.z));  // Getting the screen width and height with camera units.

        SniperWidth = SniperLeft.transform.GetComponent<BoxCollider2D>().bounds.size.x;   // Gives half of the snipers width.

        SniperLeft.transform.localPosition = new Vector3((ScreenBounds.x * -1) - (SniperWidth * 1.01f), 0, 0);   // Setting Sniper Position just outside of the screen
        SniperRight.transform.localPosition = new Vector3(ScreenBounds.x + (SniperWidth * 1.01f), 0, 0);         // Setting Sniper Position just outside of the screen

        SniperSpawner = GameObject.FindGameObjectWithTag("SniperSpawner");  // finding SniperSpawner for outro

        MinPos = transform.position.y - ((ScreenBounds.y / GameSettings.SniperCount)/2) ; // Minimal position that the Snipers can be
        MaxPos = transform.position.y + ((ScreenBounds.y / GameSettings.SniperCount)/2) ; // Maximal position that the Snipers can be
        NextPos = Random.Range(MinPos,MaxPos); // makes a first position to move to
    }


    void Update()
    {
        SniperLeftPos = SniperLeft.transform.localPosition;
        if (Outro)
        {
            _Outro();
        }
        else if (Intro)
        {
            _Intro();
        }
        else
        {
            AimFire();
        }
    }


    private void _Intro()   // Moves both snipers into screen
    {
        if (SniperLeftPos.x <= ((ScreenBounds.x * -1) + (SniperWidth/2)))
        {
            SniperLeft.transform.localPosition = SniperLeftPos + new Vector3(AnimationSpeed, 0, 0);
            SniperRight.transform.localPosition = (SniperLeftPos * -1) - new Vector3(AnimationSpeed, 0, 0);
        }
        else
        {
            Intro = false;
        }
        // Mathf.Lerp(1f,2f,3f)
    }


    private void _Outro()   // Moves both snipers out of screen if SniperSpawner is hidden
    {
        if (SniperLeftPos.x >= (ScreenBounds.x * -1) - (SniperWidth * 1.01f))
        {
            SniperLeft.transform.localPosition = SniperLeftPos + new Vector3(-AnimationSpeed, 0, 0);
            SniperRight.transform.localPosition = (SniperLeftPos * -1) - new Vector3(-AnimationSpeed, 0, 0);
        }
        else
        {
            Destroy(gameObject);
        }
    }


    private void AimFire()
    {
        if (Time.time > NextAim)    // counts every aiming cycle
        {
            NextAim = Time.time + (GameSettings.AimingTime / 7); 
            Aiming = !Aiming;
            Count += 1;
        }

        if (Count <= GameSettings.AimingCycles *2)  // if count is under  AimingCylce go aim
        {
            BeamAttack.SetActive(false);
            if (Aiming) // Snipes
            {
                BeamHighlight.SetActive(true);
            }
            else
            {
                BeamHighlight.SetActive(false);
            }  

            if ((NextPos * 0.95 < SniperLeftPos.y) && (NextPos * 1.05 < SniperLeftPos.y))     // Moves sniper to the next position
            {
                transform.position = transform.position - new Vector3(0, AnimationSpeed, 0);
            }
            else if ((NextPos * 0.95 > SniperLeftPos.y) && (NextPos * 1.05 > SniperLeftPos.y))
            {
                transform.position = transform.position + new Vector3(0, AnimationSpeed, 0);
            }    
        }
        else
        {
            BeamAttack.SetActive(true);
            if (Count == (GameSettings.AimingCycles +2) *2) // Resets all values after 2 cycles of attacking
            {
                BeamHighlight.SetActive(false);
                BeamAttack.SetActive(false);
                Count = 0;

                NextPos = Random.Range(MinPos,MaxPos);

                if (!SniperSpawner.activeInHierarchy){Outro = true;} // if SniperSpawner is not active play outro
            }
        }
    }
}